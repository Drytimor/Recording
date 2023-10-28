
def filter_events_decorator(func):
    def wrapper(**kwargs):
        if not kwargs:
            return func()
        return func().filter(**kwargs)
    return wrapper




