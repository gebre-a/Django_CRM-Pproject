# Generated by Django 5.1.3 on 2024-11-16 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sqlapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="record",
            old_name="state",
            new_name="Region",
        ),
    ]