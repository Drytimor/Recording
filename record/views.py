from django.shortcuts import HttpResponse
from django.views.generic import TemplateView

from .apis.users_api import CreateUserApi
from .selectors.events_selectors import EventsCategoryFilter


# Create your views here.


def index(request):
    return HttpResponse("hi")


class EventsHomePage(TemplateView):

    template_name = "record/events.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.__setitem__("filter", EventsCategoryFilter)
        context.__setitem__("registration", CreateUserApi.InputSerializer)
        return context


























