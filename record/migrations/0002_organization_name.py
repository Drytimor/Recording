# Generated by Django 4.2.6 on 2023-10-17 08:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("record", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="organization",
            name="name",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
