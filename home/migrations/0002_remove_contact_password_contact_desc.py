# Generated by Django 4.2.5 on 2023-10-25 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contact",
            name="password",
        ),
        migrations.AddField(
            model_name="contact",
            name="desc",
            field=models.TextField(default=2000),
            preserve_default=False,
        ),
    ]
