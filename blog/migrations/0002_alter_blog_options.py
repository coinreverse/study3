# Generated by Django 5.0 on 2024-03-09 04:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog",
            options={"ordering": ["-created_time"]},
        ),
    ]
