from django.urls import path, include
from . import views
from .apis import EventsListApi


events_api_patterns = [
    path("events/", EventsListApi.as_view(), name='event')
]

urlpatterns = [
    path("", views.index, name='index'),
    path("events/", views.EventsHomePage.as_view(), name='event'),
    path("api/", include(events_api_patterns)),
]


