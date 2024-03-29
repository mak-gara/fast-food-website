# Generated by Django 4.1.1 on 2022-12-22 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_deliveryorder_payment_pickuporder_payment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deliveryorder',
            options={'verbose_name': 'Доставка', 'verbose_name_plural': 'Доставка'},
        ),
        migrations.AlterModelOptions(
            name='pickuporder',
            options={'verbose_name': 'Самовивіз', 'verbose_name_plural': 'Самовивіз'},
        ),
        migrations.AlterField(
            model_name='deliveryorder',
            name='entrance',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name="Під'їзд"),
        ),
        migrations.AlterField(
            model_name='deliveryorder',
            name='flat',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Квартири'),
        ),
        migrations.AlterField(
            model_name='deliveryorder',
            name='floor',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Поверх'),
        ),
    ]
