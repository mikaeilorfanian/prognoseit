from django.contrib import admin
from game.models import Bet, Event


class BetAdmin(admin.ModelAdmin):
    pass


class EventAdmin(admin.ModelAdmin):
    pass


admin.site.register(Bet, BetAdmin)
admin.site.register(Event, EventAdmin)
