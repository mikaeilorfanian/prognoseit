from django.conf.urls import url
from .views import EventList

urlpatterns = [
    url(r'^events/$', EventList.as_view()),
    url(r'^events/(?P<pk>[0-9]+)/$', EventList.as_view()),
]
