from django.shortcuts import HttpResponse
from django.views.generic import TemplateView
from .selectors.events import EventsCategoryFilter


# Create your views here.


def index(request):
    return HttpResponse("hi")


class EventsHomePage(TemplateView):

    template_name = "record/events.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault("filter", EventsCategoryFilter)
        return context


























