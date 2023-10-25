from record.decorators import filter_decorator
from record.selectors.home import all_events


class HomePage:

    def __init__(self, activity):
        self.activity = activity

    def get_all_events(self):
        if self.activity == "all":
            return filter_decorator(all_events)()

        elif self.activity == "education":
            return filter_decorator(all_events)(organization__activity__exact="ED")

        elif self.activity == "science":
            return filter_decorator(all_events)(organization__activity__exact="SC")

        elif self.activity == "tourism":
            return filter_decorator(all_events)(organization__activity__exact="TR")

        elif self.activity == "sport":
            return filter_decorator(all_events)(organization__activity__exact="SP")

        elif self.activity == "entertainment":
            return filter_decorator(all_events)(organization__activity__exact="ET")

        elif self.activity == "sundry":
            return filter_decorator(all_events)(organization__activity__exact="SN")







