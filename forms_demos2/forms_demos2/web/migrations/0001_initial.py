# Generated by Django 4.1.2 on 2022-10-24 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TodoModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=30)),
                ("text", models.CharField(blank=True, max_length=500, null=True)),
                ("is_done", models.BooleanField(blank=True, default=False)),
                ("priority", models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
