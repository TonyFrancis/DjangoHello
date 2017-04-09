import datetime

from django.db import models

class Event(models.Model):
    """Calendar Event and methods."""
    __tablename__ = "event"
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    location = models.CharField(max_length=300)
    description = models.CharField(max_length=5000)

    def __init__(self):
        self.start_time = datetime.datetime.utcnow()

    def get_by_id(self, id):
        """Get Event if Present"""
        oEvent = Event.object.get(pk=id)
        if oEvent:
            return oEvent, None
        return None, "Event not Present"

    @classmethod
    def create(cls, data):
        """Creating Event."""
        oEvent = cls()
        oEvent.start_time = data["start_time"]
        oEvent.end_time = data["end_time"]
        oEvent.location = data["location"]
        oEvent.description = data["description"]
        oEvent.save()
        return oEvent

    def delete(self):
        """Delete Event."""
        self.delete()

    def update(self, data):
        """Updating Event."""
        self.start_time = data["start_time"]
        self.end_time = data["end_time"]
        self.location = data["location"]
        self.description = data["description"]
        self.save()
        return self

    @classmethod
    def get_list(cls,start_time, end_time):
        """
        Return list of all calendar event in a peroid.

        @param start_time
        @param end_time
        """
        return cls.objects.filter(start_time__gt = start_time)\
                .filter(end_time__lt = end_time).all()

    def as_dict(self):
        """Convert Event as dict."""
        return {
            "start_time" : self.start_time,
            "end_time" : self.end_time,
            "location" : self.location,
            "description" : self.description,
            "id" : self.id
        }

    @classmethod
    def get_events(cls, time_range):
        """
        Get all event between time_range.

        @param time_range keys present start_time, end_time.
        """
        now = datetime.datetime.utcnow()
        month = (now.month % 12) + 1
        start_time = time_range.get(
            'start_time',
            datetime.datetime(now.year,month,1)
            )
        end_time = time_range.get(
            'end_time',
            datetime.datetime(now.year,month + 1,1)
            )
        lEvent = cls.get_list(start_time, end_time)
        return [ oEvent.as_dict() for oEvent in lEvent ]
