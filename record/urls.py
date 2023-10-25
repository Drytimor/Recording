from django.urls import path
from . import views

urlpatterns = [

    path("", views.index, name='index'),
    path("<str:activity>/", views.AllEvents.as_view(), name='activity'),

]



