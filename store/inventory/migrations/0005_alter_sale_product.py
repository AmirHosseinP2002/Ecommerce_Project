# Generated by Django 5.0.3 on 2024-03-27 12:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_sale_product'),
        ('products', '0009_ipaddress_producthit_product_hits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_records', to='products.product'),
        ),
    ]
