# Generated by Django 5.0.3 on 2024-04-01 11:13

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20240401_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
