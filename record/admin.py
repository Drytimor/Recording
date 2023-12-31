from django.contrib import admin
from django.contrib.auth.admin import User, UserAdmin as BaseUserAdmin
from .models import Organizations, Employees, Events, Customers, Recordings, HistoryRecordings


# Register your models here.

admin.site.unregister(User)


class CustomerInline(admin.StackedInline):
    model = Customers
    can_delete = False
    verbose_name = "профиль"


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = [CustomerInline]


@admin.register(Organizations)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ["name", "user", "activitys", ]
    empty_value_display = "-empty-"


@admin.register(Employees)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = ["organization", "firstname", "lastname", "email", ]


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):

    list_display = ["name", "organization", "price_event", "date_event", "time_events",
                    "status_tariff", "status_opening", "limit_clients", "quantity_clients"]
    filter_horizontal = ('employee',)
    empty_value_display = "-empty-"

    @admin.display(description="Start time - End time")
    def time_events(self, obj):
        return f"{obj.start_time}-{obj.end_time}"


@admin.register(Recordings)
class RecordingAdmin(admin.ModelAdmin):
    list_display = ["event", "customer"]


@admin.register(HistoryRecordings)
class HistoryRecordingAdmin(admin.ModelAdmin):
    list_display = ["recording_id", "event_id", "customer_id", "status_recording", "date_recording"]
