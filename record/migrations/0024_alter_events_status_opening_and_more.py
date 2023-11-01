# Generated by Django 4.2.6 on 2023-10-28 13:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("record", "0023_remove_events_check_status_tariff_events_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="events",
            name="status_opening",
            field=models.CharField(
                choices=[("open", "открытые"), ("close", "закрытые")],
                default="open",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="events",
            name="status_tariff",
            field=models.CharField(
                choices=[("paid", "платные"), ("free", "бесплатные")], max_length=4
            ),
        ),
    ]