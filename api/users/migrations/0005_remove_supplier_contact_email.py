# Generated by Django 3.2.3 on 2025-03-06 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_auto_20250306_1830"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="supplier",
            name="contact_email",
        ),
    ]
