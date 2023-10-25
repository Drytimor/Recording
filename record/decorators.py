def filter_decorator(func):
    def wrapper(**kwargs):
        if not kwargs:
            return func
        queryset = func().filter(**kwargs)
        return queryset
    return wrapper




