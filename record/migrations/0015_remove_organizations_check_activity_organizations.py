# Generated by Django 4.2.6 on 2023-10-25 12:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("record", "0014_remove_customers_check_hobby_customers_and_more"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="organizations",
            name="check_activity_organizations",
        ),
    ]
