from django_filters import FilterSet, ChoiceFilter
from record.models import Events, ActivitysChoices, PaymentTariffChoices, StatusOpeningChoices
from django.forms import widgets


class EventsCategoryFilter(FilterSet):

    activitys = ChoiceFilter(field_name='organization__activitys__name',
                             lookup_expr='exact',
                             label='activitys',
                             widget=widgets.Select,
                             choices=ActivitysChoices.choices,
                             empty_label='Все'
                             )
    tariff = ChoiceFilter(field_name='status_tariff',
                          lookup_expr='exact',
                          label='tariff',
                          widget=widgets.Select,
                          choices=PaymentTariffChoices.choices,
                          empty_label='Все',
                          )
    open = ChoiceFilter(field_name='status_opening',
                        lookup_expr='exact',
                        label='open',
                        widget=widgets.Select,
                        choices=StatusOpeningChoices.choices,
                        empty_label='Все',
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
    return EventsCategoryFilter(filters, qs)





