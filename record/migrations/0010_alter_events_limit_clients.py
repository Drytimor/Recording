# Generated by Django 4.2.6 on 2023-10-19 07:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("record", "0009_rename_events_employee_events_employee"),
    ]

    operations = [
        migrations.AlterField(
            model_name="events",
            name="limit_clients",
            field=models.SmallIntegerField(),
        ),
    ]
