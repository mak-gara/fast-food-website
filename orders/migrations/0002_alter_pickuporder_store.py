# Generated by Django 4.1.1 on 2022-12-25 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_delete_deliveryorder_delete_pickuporder'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pickuporder',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.store', verbose_name='Магазин'),
        ),
    ]
