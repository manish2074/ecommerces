# Generated by Django 2.2.2 on 2019-08-11 14:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
