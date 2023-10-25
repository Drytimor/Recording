from django.shortcuts import HttpResponse
from django.views.generic.base import TemplateView


from .services.home import HomePage


# Create your views here.


def index(request):
    return HttpResponse("hi")


class AllEvents(TemplateView):

    template_name = "record/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events = HomePage(kwargs.get("activity"))
        context["detail_events"] = events.get_all_events()
        return context






















