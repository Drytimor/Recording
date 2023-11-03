from django.shortcuts import HttpResponse
from django.views.generic import TemplateView
from .selectors.events import events_category

# Create your views here.


def index(request):
    return HttpResponse("hi")


class EventsHomePage(TemplateView):

    template_name = "record/events.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault("category", events_category(self.request.GET))
        return context


























