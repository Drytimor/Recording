# Generated by Django 4.2.6 on 2023-10-19 07:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("record", "0008_events_check_time_events"),
    ]

    operations = [
        migrations.RenameField(
            model_name="events",
            old_name="events_employee",
            new_name="employee",
        ),
    ]