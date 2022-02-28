from rest_framework import serializers

from events.models import Event, EventStatus


class EventStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventStatus
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):

    # event_status = EventStatusSerializer()

    class Meta:
        model = Event
        fields = [
            "client",
            "contract",
            "event_status",
            "date_created",
            "date_updated",
            "attendees",
            "event_date",
            "notes",
            "is_finished",
        ]
