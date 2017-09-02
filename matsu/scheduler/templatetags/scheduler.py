
from calendar import Calendar
from collections import namedtuple
from datetime import timedelta
from functools import lru_cache

from django import template
from django.utils import timezone

from matsu.scheduler.models import Event

register = template.Library()

Month = namedtuple('Month', ['first_day', 'days'])

Day = namedtuple('Day', ['date', 'events'])

cal = Calendar()


def add_month(date, count=1):
    for unused in range(count):
        date = (date + timedelta(days=32)).replace(day=1)
    return date


@lru_cache(maxsize=128)
class RepeatingDays(object):

    def __init__(self, date, until):
        self.date = date
        self.until = until

        self._daily = None
        self._weekly = None
        self._bi_weekly = None
        self._monthly = None
        self._yearly = None

    @property
    def daily(self):
        if self._daily is None:
            self._daily = set(self.days_gen(self.date, self.until))
        return self._daily

    @property
    def weekly(self):
        if self._weekly is None:
            self._weekly = set(self.weeks_gen(self.date, self.until))
        return self._weekly

    @property
    def bi_weekly(self):
        if self._bi_weekly is None:
            self._bi_weekly = set(self.weeks_gen(self.date, self.until, 2))
        return self._bi_weekly

    @property
    def monthly(self):
        if self._monthly is None:
            self._monthly = set(self.months_gen(self.date, self.until))
        return self._monthly

    @property
    def yearly(self):
        if self._yearly is None:
            self._yearly = set(self.years_gen(self.date, self.until))
        return self._yearly

    @staticmethod
    def days_gen(date, until):
        td_day = timedelta(days=1)
        new_date = date
        while new_date <= until:
            yield new_date
            new_date += td_day

    @staticmethod
    def weeks_gen(date, until, weeks=1):
        td_week = timedelta(weeks=weeks)
        new_date = date
        while new_date <= until:
            yield new_date
            new_date += td_week

    @staticmethod
    def months_gen(date, until):
        year, month = date.year, date.month
        new_date = date
        while new_date <= until:
            yield new_date
            month += 1
            if month == 13:
                year += 1
                month = 1
            try:
                new_date = new_date.replace(year=year, month=month)
            except ValueError:
                continue  # Leap year

    @staticmethod
    def years_gen(date, until):
        year = date.year
        new_date = date
        while new_date <= until:
            yield new_date
            year += 1
            try:
                new_date = new_date.replace(year=year)
            except ValueError:
                continue  # Leap year


def is_belongs_to(date, event):
    if date < event.valid_from or date > event.valid_until:
        return False

    repeating = RepeatingDays(event.valid_from, event.valid_until)
    if (
        event.repeat == Event.DO_NOT_REPEAT and
        (event.valid_from == event.valid_until and date != event.valid_from)
    ):
        return False
    if event.repeat == Event.DAILY and date not in repeating.daily:
        return False
    if event.repeat == Event.WEEKLY and date not in repeating.weekly:
        return False
    if event.repeat == Event.BI_WEEKLY and date not in repeating.bi_weekly:
        return False
    if event.repeat == Event.MONTHLY and date not in repeating.monthly:
        return False
    if event.repeat == Event.YEARLY and date not in repeating.yearly:
        return False

    return True


@register.assignment_tag
def get_scheduler_events(months=2):
    calendar = []

    start = timezone.now().date().replace(day=1)
    stop = add_month(start, months + 1) - timedelta(days=1)

    events = Event.objects.prefetch_related(
        'cancelled'
    ).filter(
        valid_from__lt=stop, valid_until__gte=start
    ).order_by(
        'start'
    )

    months_first_dates = (add_month(start, i) for i in range(months))
    for month in (Month(first_date, []) for first_date in months_first_dates):
        days = cal.itermonthdates(month.first_day.year, month.first_day.month)
        for date in days:
            day = Day(date, [])
            if day.date.month == month.first_day.month:
                for event in events:
                    if is_belongs_to(day.date, event):
                        day.events.append(event)
            month.days.append(day)
        calendar.append(month)

    return calendar


@register.filter_function
def is_cancelled_for_day(event, day):
    return event.is_cancelled_for_day(day)
