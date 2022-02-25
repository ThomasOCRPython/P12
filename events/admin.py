from django.contrib import admin
from events import models


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    

    list_display = ('client', 'contract', 'event_status', "date_created", "date_updated",
                  'attendees', 'event_date', 'notes','is_finished')

    list_filter = ('client', 'event_status', 'date_created')

@admin.register(models.EventStatus)
class EventStatusAdmin(admin.ModelAdmin):
    

    field_display = ('event_status')

    field_filter = ('event_status')
