# Generated by Django 4.1.2 on 2022-10-05 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0005_manager_level_manager_salary_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="manager",
            name="level",
            field=models.IntegerField(
                choices=[(1, "Supervisor"), (2, "Manager"), (3, "Director")],
                null=True,
                verbose_name="Proficiency level",
            ),
        ),
    ]
