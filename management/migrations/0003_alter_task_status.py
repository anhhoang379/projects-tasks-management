# Generated by Django 5.0 on 2023-12-15 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0002_staff"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.CharField(
                choices=[
                    ("Not Started", "Not Started"),
                    ("In Progress", "In Progress"),
                    ("Completed", "Completed"),
                ],
                default="Not Started",
                max_length=20,
            ),
        ),
    ]
