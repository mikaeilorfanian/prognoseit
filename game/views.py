from rest_framework.views import APIView
from rest_framework import generics, viewsets
from rest_framework import mixins

from .models import Event
from .serializers import EventSerializer


class EventList(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """
    queryset = Event.objects.all().order_by('-created_at')
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveAPIView):
    queryset = Event.objects.all().order_by('-created_at')
    serializer_class = EventSerializer
