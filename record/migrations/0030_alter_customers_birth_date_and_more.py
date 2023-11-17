# Generated by Django 4.2.6 on 2023-11-16 07:42

from django.db import migrations, models
import record.validators


class Migration(migrations.Migration):
    dependencies = [
        ("record", "0029_alter_customers_birth_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customers",
            name="birth_date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="customers",
            name="phone_number",
            field=models.CharField(
                max_length=20,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="employees",
            name="phone_number",
            field=models.CharField(
                max_length=20,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="organizations",
            name="phone_number",
            field=models.CharField(
                max_length=20,
                unique=True,
            ),
        ),
    ]