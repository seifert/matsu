
from django.contrib import admin

from matsu.scheduler.models import Category, Event, CancelledEvent


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('title',)
    ordering = ('title',)
    search_fields = ('title',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = (
        'title', 'category', 'valid_from', 'start',
        'valid_until', 'stop', 'repeat')
    ordering = ('-valid_from', '-start')
    search_fields = ('title',)


@admin.register(CancelledEvent)
class CancelledEventAdmin(admin.ModelAdmin):

    list_display = (
        'events_as_short_str', 'valid_from', 'valid_until',
        'short_description')
    ordering = ('-valid_from',)
