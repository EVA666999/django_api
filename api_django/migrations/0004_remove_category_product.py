# Generated by Django 3.2.3 on 2025-02-22 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_django', '0003_category_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='product',
        ),
    ]
