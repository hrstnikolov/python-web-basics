# Generated by Django 4.1.2 on 2022-10-12 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0011_alter_employee_city_alter_employee_review_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="AccessCard",
            fields=[
                (
                    "employee",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="web.employee",
                    ),
                ),
            ],
        ),
    ]
