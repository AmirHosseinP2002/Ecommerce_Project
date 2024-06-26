# Generated by Django 5.0.3 on 2024-03-23 09:07

import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
            options={
                'verbose_name': 'Time Slot',
                'verbose_name_plural': 'Time Slots',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=64)),
                ('province', models.CharField(max_length=64)),
                ('building_number', models.PositiveSmallIntegerField()),
                ('unit', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('postal_code', models.CharField(max_length=10)),
                ('receiver_first_name', models.CharField(max_length=64)),
                ('receiver_last_name', models.CharField(max_length=64)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='IR')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_date', models.DateField()),
                ('max_capacity', models.PositiveSmallIntegerField(default=10)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shipping.address')),
                ('delivery_time_slot', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shipping.timeslot')),
            ],
            options={
                'verbose_name': 'Shipping',
                'verbose_name_plural': 'Shippings',
            },
        ),
    ]
