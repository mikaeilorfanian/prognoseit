from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

from .models import Event
from .serializers import EventSerializer


class EventList(generics.ListCreateAPIView):
    """
    API endpoint that allows events to be viewed or edited.
    """
    queryset = Event.objects.all().order_by('-created_at')
    serializer_class = EventSerializer

