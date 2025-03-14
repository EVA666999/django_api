# Generated by Django 5.1.7 on 2025-03-14 02:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api_django", "0014_purchasehistory"),
    ]

    operations = [
        migrations.RenameField(
            model_name="purchasehistory",
            old_name="purchased_at",
            new_name="purchase_date",
        ),
        migrations.AddField(
            model_name="purchasehistory",
            name="order",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="api_django.order",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="purchasehistory",
            name="price",
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="purchasehistory",
            name="quantity",
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="purchasehistory",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order_items",
                to="api_django.product",
            ),
        ),
    ]
