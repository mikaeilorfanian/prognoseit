from django.conf.urls import url
from .views import BetList, EventList

urlpatterns = [
    url(r'^events/$', EventList.as_view()),
    url(r'^bets/$', BetList.as_view()),
]
