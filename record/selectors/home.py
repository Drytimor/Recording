from ..models import Events
from ..decorators import filter_events_decorator


@filter_events_decorator
def all_events():
    return (Events.objects.values("name", "start_time", "end_time",
                                  "date_event", "status_tariff",
                                  "status_opening", "limit_clients",
                                  "quantity_clients", "price_event",
                                  "organization__name"))


