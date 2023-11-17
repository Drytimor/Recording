# Generated by Django 4.2.6 on 2023-11-15 11:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("record", "0026_remove_customers_hobby_alter_activitys_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="employees",
            name="date_joined",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="organizations",
            name="date_joined",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
