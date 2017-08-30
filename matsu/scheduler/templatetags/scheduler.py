
from calendar import Calendar
from collections import defaultdict
from datetime import timedelta

from django import template
from django.utils import timezone

from matsu.scheduler.models import Event, CancelledEvent

register = template.Library()

cal = Calendar()


class FakeEvens(list):
    def __init__(self):
        self.extend(
            ["Cvičení děti", "Cvičení trenéři a trenérky",
             "Večeře", "Pivo", "Spát"]
        )


@register.assignment_tag
def get_scheduler_events(months=2):
    calendar = []
    start = timezone.now().date().replace(day=1)
    stop = start
    for unused in range(months):
        year = stop.year
        month = stop.month
        month_struct = [
            stop, [[d, None] for d in cal.itermonthdates(year, month)]
        ]
        calendar.append(month_struct)
        stop = (stop + timedelta(days=32)).replace(day=1)

    events = Event.objects.filter(valid_from__lt=stop, valid_until__gte=start)
    cancelled_events = CancelledEvent.objects.filter(events__in=[e.id for e in events])

    dates_events = defaultdict(FakeEvens)
    # TODO: fill dates_events

    for month_struct in calendar:
        for day in month_struct[1]:
            day[1] = dates_events[day[0]]

    return calendar
