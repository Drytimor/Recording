import django_filters
from record.models import Events


class EventsFilter(django_filters.FilterSet):

    class Meta:
        model = Events
        fields = ["name"]

