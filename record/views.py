from django.shortcuts import HttpResponse
from django.views.generic import TemplateView
from .services.home import get_context_events

# Create your views here.


def index(request):
    return HttpResponse("hi")


class EventsHomePage(TemplateView):

    template_name = "record/events.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context_events(self.request.GET))
        return context


























