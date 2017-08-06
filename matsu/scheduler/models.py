
from django.db import models
from django.utils.text import Truncator
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):

    title = models.CharField(_("Title"), max_length=100)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.title


class Event(models.Model):

    REPEAT_CHOICES = (
        (1, _("Do not repeat")),
        (2, _("Daily")),
        (3, _("Weekly")),
        (4, _("Bi-weekly")),
        (5, _("Monthly")),
        (6, _("Yearly")),
    )

    title = models.CharField(_("Title"), max_length=100)
    description = models.TextField(_("Description"), blank=True)
    category = models.ForeignKey(
        Category, verbose_name=_("Category"), blank=True, null=True)
    valid_from = models.DateField(_("Valid from"), db_index=True)
    start = models.TimeField(_("Start"))
    stop = models.TimeField(_("Stop"), blank=True, null=True)
    repeat = models.IntegerField(
        _("Repeat"), choices=REPEAT_CHOICES, blank=True, null=True)
    valid_until = models.DateField(
        _("Valid until"), blank=True, null=True, db_index=True)

    class Meta:
        verbose_name = _("event")
        verbose_name_plural = _("events")

    def __str__(self):
        return self.title

    def short_description(self):
        return Truncator(self.description).words(50, truncate=' ...')


class CancelledEvent(models.Model):

    events = models.ManyToManyField(
        Event, related_name='cancelled', verbose_name=_("Events"))
    valid_from = models.DateField(_("Valid from"), db_index=True)
    valid_until = models.DateField(_("Valid until"), db_index=True)
    description = models.TextField(_("Description"), blank=True)

    class Meta:
        verbose_name = _("Cancelled event")
        verbose_name_plural = _("Cancelled events")

    def short_description(self):
        return Truncator(self.description).words(10, truncate=' ...')
    short_description.short_description = _("Description")

    def events_as_str(self):
        return ", ".join(e.title for e in self.events.all())
    events_as_str.short_description = _("Events")

    def events_as_short_str(self):
        return Truncator(self.events_as_str()).words(10, truncate=' ...')
    events_as_short_str.short_description = _("Events")
