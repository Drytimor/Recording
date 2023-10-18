from django.shortcuts import render
from .models import Events

# Create your views here.


def index(request):
    all_events = Events.objects.values("name", "start_time", "end_time", "date_event",
                                       "status_tariff", "status_opening",
                                       "limit_clients", "quantity_clients",
                                       "price_event", "organization__name")
    return render(request, "record/home.html",
                  context={
                      "all_events": all_events})



