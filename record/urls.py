from django.urls import path
from . import views

urlpatterns = [

    path("", views.index, name='index'),
    path("record/<str:activity>/", views.EventsHomePage.as_view(), name='activity'),

]



