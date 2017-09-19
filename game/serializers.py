from rest_framework import serializers
from .models import Bet, Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('url', 'id', 'title',)
        
        
class BetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = ('url', 'event', 'player', 'outcome', 'quantity')
