from rest_framework import serializers
from ..models.events import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
