from django_filters import FilterSet, MultipleChoiceFilter
from record.models import Events, ActivitysChoices, PaymentTariffChoices, StatusOpeningChoices
from django.forms import widgets


class EventsCategoryFilter(FilterSet):

    activitys = MultipleChoiceFilter(field_name='organization__activitys__name',
                                     label='activitys',
                                     widget=widgets.CheckboxSelectMultiple,
                                     choices=ActivitysChoices.choices,
                                     )
    tariff = MultipleChoiceFilter(field_name='status_tariff',
                                  label='tariff',
                                  widget=widgets.CheckboxSelectMultiple,
                                  choices=PaymentTariffChoices.choices,
                                  )
    open = MultipleChoiceFilter(field_name='status_opening',
                                label='open',
                                widget=widgets.CheckboxSelectMultiple,
                                choices=StatusOpeningChoices.choices,
                                )

    class Meta:
        model = Events
        fields = ["activitys", "tariff",
                  "open"]


def events_category(filters=None) -> EventsCategoryFilter:
    filters = filters or {}
    qs = Events.objects.values("name", "start_time", "end_time",
                               "date_event", "status_tariff",
                               "status_opening", "limit_clients",
                               "quantity_clients", "price_event",
                               "organization__name",
                               )
    return EventsCategoryFilter(filters, qs).qs





