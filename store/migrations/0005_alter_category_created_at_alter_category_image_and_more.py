# Generated by Django 4.1.1 on 2022-10-09 06:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_category_options_alter_popularcategory_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата створення'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='categories/%Y/%m/%d/', verbose_name='Зображення'),
        ),
        migrations.AlterField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Активність'),
        ),
        migrations.AlterField(
            model_name='popularcategory',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активність'),
        ),
        migrations.AlterField(
            model_name='popularcategory',
            name='item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.category', verbose_name='Категорія'),
        ),
        migrations.AlterField(
            model_name='popularcategory',
            name='sequence_number',
            field=models.PositiveSmallIntegerField(verbose_name='Порядковий номер'),
        ),
        migrations.AlterField(
            model_name='popularcategory',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата оновлення'),
        ),
        migrations.AlterField(
            model_name='product',
            name='calories',
            field=models.PositiveSmallIntegerField(verbose_name='Калорійність'),
        ),
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(related_name='products', to='store.category', verbose_name='Категорії'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата створення'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount_percentage',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100, message='Введене значення перевищує максимально допустиме')], verbose_name='Знижка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products/%Y/%m/%d/', verbose_name='Зображення'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Активність'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='Наявність'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ціна'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(db_index=True, max_length=255, verbose_name='Найменування'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата оновлення'),
        ),
        migrations.AlterField(
            model_name='product',
            name='volume',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Об'єм"),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Вага'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активність'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='sequence_number',
            field=models.PositiveSmallIntegerField(verbose_name='Порядковий номер'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата оновлення'),
        ),
        migrations.AlterField(
            model_name='slideritem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата створення'),
        ),
        migrations.AlterField(
            model_name='slideritem',
            name='image',
            field=models.ImageField(upload_to='slider_images/%Y/%m/%d/', verbose_name='Зображення'),
        ),
        migrations.AlterField(
            model_name='slideritem',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Активність'),
        ),
        migrations.AlterField(
            model_name='store',
            name='adress',
            field=models.CharField(db_index=True, max_length=255, verbose_name='Адреса'),
        ),
        migrations.AlterField(
            model_name='store',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата створення'),
        ),
        migrations.AlterField(
            model_name='store',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активність'),
        ),
    ]
