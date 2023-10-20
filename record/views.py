import django.views.generic.list
from django.shortcuts import HttpResponse
from django.views.generic.list import ListView
from .models import Events

# Create your views here.


def index(request):
    return HttpResponse("hi")

class AllEvents(ListView):

    queryset = (Events.objects
                .values("name", "start_time", "end_time",
                        "date_event", "status_tariff",
                        "status_opening", "limit_clients", "quantity_clients",
                        "price_event", "organization__name"))



# def activity(request, activity):
#     all_events = (Events.objects
#                   .values("name", "start_time", "end_time",
#                           "date_event", "status_tariff",
#                           "status_opening", "limit_clients", "quantity_clients",
#                           "price_event", "organization__name"))
#     if activity == "all":
#         detail_events = all_events
#         return render(request, "record/home.html", context={
#             "detail_events": detail_events})
#
#     elif activity == "education":
#         detail_events = all_events.filter(organization__activity__exact="ED")
#         return render(request, "record/home.html", context={
#             "detail_events": detail_events})
#
#     elif activity == "science":
#         detail_events = all_events.filter(organization__activity__exact="SC")
#         return render(request, "record/home.html", context={
#             "detail_events": detail_events})
#
#     elif activity == "tourism":
#         detail_events = all_events.filter(organization__activity__exact="TR")
#         return render(request, "record/home.html", context={
#             "detail_events": detail_events})
#
#     elif activity == "sport":
#         detail_events = all_events.filter(organization__activity__exact="SP")
#         return render(request, "record/home.html", context={
#             "detail_events": detail_events})
#
#     elif activity == "entertainment":
#         detail_events = all_events.filter(organization__activity__exact="ET")
#         return render(request, "record/home.html", context={
#             "detail_events": detail_events})
#
#     elif activity == "sundry":
#         detail_events = all_events.filter(organization__activity__exact="SN")
#         return render(request, "record/home.html", context={
#             "detail_events": detail_events})








