# Generated by Django 5.0.3 on 2024-03-09 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_description_alter_product_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=256, unique=True),
        ),
    ]
