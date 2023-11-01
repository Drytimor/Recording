from ..selectors.home import events_category


def get_context_events(request_get):
    return {
        "category": events_category(request_get)
    }









