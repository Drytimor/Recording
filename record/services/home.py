from record.selectors.home import all_events
from ..forms import FilterEventsForm
from ..models import ActivitysChoices


class HomePage:

    def __init__(self, activity, filter):
        self._activity = activity
        self.status_tariff = filter.getlist("tariff")
        self.status_opening = filter.getlist("open")

    @property
    def activity(self):
        if self._activity == 'all':
            return [activity for activity in ActivitysChoices.values]
        return [self._activity]

    def _get_events_activity(self):
        if not self.status_opening:
            if not self.status_tariff:
                return all_events(organization__activity__in=self.activity)

            return all_events(organization__activity__in=self.activity,
                              status_tariff__in=self.status_tariff)

        elif not self.status_tariff:
            return all_events(organization__activity__in=self.activity,
                              status_opening__in=self.status_opening)
        return all_events(organization__activity__in=self.activity,
                          status_tariff__in=self.status_tariff,
                          status_opening__in=self.status_opening)

    def get_context_events(self):
        return {
            "detail_events": self._get_events_activity(),
            "activity_events": ActivitysChoices.choices,
            "form": FilterEventsForm,
        }









