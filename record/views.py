from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.views.generic import TemplateView, CreateView, View
from django.contrib.auth.decorators import login_required
from .forms import CreateProfileForm, CreateUserForm
from .selectors.events_selectors import EventsCategoryFilter
from django.db import transaction

# Create your views here.


def index(request):
    return HttpResponse("hi")


class EventsHomePage(TemplateView):

    template_name = "record/events.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.__setitem__("filter", EventsCategoryFilter)
        context.__setitem__("create_user", CreateUserForm)
        context.__setitem__("create_profile", CreateProfileForm)
        return context


class CreateUserView(View):

    user_form = CreateUserForm
    profile_form = CreateProfileForm

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form_user = self.user_form(request.POST)
        from_profile = self.profile_form(request.POST)
        if form_user.is_valid() and from_profile.is_valid():
            form_user.save()
            # from_profile.save()
            return JsonResponse({
                "success": True
            })
        else:
            return JsonResponse({
                "error_user": form_user.errors,
                "error_profile": from_profile.errors
            })
























