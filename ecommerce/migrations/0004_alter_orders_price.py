# Generated by Django 4.2.4 on 2023-08-24 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_orders_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='price',
            field=models.IntegerField(blank=True, default=1500, null=True),
        ),
    ]
