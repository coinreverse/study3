# Generated by Django 5.0 on 2024-03-12 12:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0005_blog_readed_num"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="readed_num",
        ),
        migrations.CreateModel(
            name="ReadNum",
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
                ("read_num", models.IntegerField(default=0)),
                (
                    "blog",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.blog"
                    ),
                ),
            ],
        ),
    ]
