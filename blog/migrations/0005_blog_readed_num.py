# Generated by Django 5.0 on 2024-03-12 07:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_alter_blog_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="readed_num",
            field=models.IntegerField(default=0),
        ),
    ]