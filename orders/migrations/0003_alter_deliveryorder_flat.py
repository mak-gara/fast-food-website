# Generated by Django 4.1.1 on 2022-12-27 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_pickuporder_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryorder',
            name='flat',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Квартира'),
        ),
    ]