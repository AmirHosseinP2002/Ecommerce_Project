# Generated by Django 5.0.3 on 2024-03-29 11:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shippings', to='shipping.address'),
        ),
    ]
