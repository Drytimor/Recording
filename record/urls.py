from django.urls import path, include
from . import views
from record.apis.events_api import EventsListApi
from .apis.users_api import CreateUserApi

events_api_patterns = [
    path("events-list/", EventsListApi.as_view()),
    path("registration/", CreateUserApi.as_view())
]

urlpatterns = [
    path("", views.index, name='index'),
    path("events/", views.EventsHomePage.as_view(), name='event'),
    path("api/", include(events_api_patterns)),
]


