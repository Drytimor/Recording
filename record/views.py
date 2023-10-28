from django.shortcuts import HttpResponse
from django.views.generic import TemplateView, ListView
from .services.home import HomePage

# Create your views here.


def index(request):
    return HttpResponse("hi")


class EventsHomePage(TemplateView):

    template_name = "record/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events = HomePage(kwargs.get("activity"), self.request.GET)
        context.update(events.get_context_events())
        return context


























