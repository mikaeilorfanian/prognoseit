from rest_framework.views import APIView
from rest_framework import generics, viewsets
from rest_framework import mixins

from .models import Bet, Event
from .serializers import BetSerializer, EventSerializer


class EventList(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """
    queryset = Event.objects.all().order_by('-created_at')
    serializer_class = EventSerializer


class BetList(viewsets.ReadOnlyModelViewSet):
    queryset = Bet.objects.all().order_by()
    serializer_class = BetSerializer
