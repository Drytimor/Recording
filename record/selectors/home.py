from ..models import Events


def all_events():
    queryset = (Events.objects.values("name", "start_time", "end_time",
                                      "date_event", "status_tariff",
                                      "status_opening", "limit_clients",
                                      "quantity_clients", "price_event",
                                      "organization__name"))
    return queryset


