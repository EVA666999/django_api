# Generated by Django 5.1.7 on 2025-03-13 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api_django", "0009_productreview_delete_video"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="products_images/"
            ),
        ),
    ]
