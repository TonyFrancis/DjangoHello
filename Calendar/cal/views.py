# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from django.http import HttpResponse
from .serializers import EventSerializer
from .models import Event
from django.http import JsonResponse

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

def index(request):
    import datetime
    start = datetime.datetime.utcnow()
    end = datetime.datetime(2020,1,1)
    oEvents = EventSerializer(Event.get_list(start,end),many=True)

    return JsonResponse({ "data": oEvents.data })
