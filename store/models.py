from django.db import models
from django.urls import reverse_lazy
from django.core.validators import MaxValueValidator
from django.utils.safestring import mark_safe
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    '''Food category'''

    title = models.CharField(verbose_name='Найменування',
                             max_length=255, db_index=True)
    image = models.ImageField(
        verbose_name='Зображення', upload_to='categories/%Y/%m/%d/')
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(verbose_name='Активність', default=False)
    created_at = models.DateTimeField(
        verbose_name='Дата створення', auto_now_add=True)

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def get_absolute_url(self):
        return reverse_lazy('store:products', args=[self.slug])

    def __str__(self):
        return self.title


class Product(models.Model):
    '''Product on the menu'''

    title = models.CharField(verbose_name='Найменування',
                             max_length=255, db_index=True)
    description = models.TextField(verbose_name='Опис')
    image = models.ImageField(
        verbose_name='Зображення', upload_to='products/%Y/%m/%d/')
    price = models.PositiveIntegerField(verbose_name='Ціна')
    discount_percentage = models.PositiveIntegerField(
        verbose_name='Знижка', blank=True, null=True, validators=[MaxValueValidator(100, message='Введене значення перевищує максимально допустиме')])
    weight = models.PositiveSmallIntegerField(
        verbose_name='Вага', blank=True, null=True)
    volume = models.PositiveSmallIntegerField(
        verbose_name='Об\'єм', blank=True, null=True)
    calories = models.PositiveSmallIntegerField(verbose_name='Калорійність')
    categories = models.ManyToManyField(
        Category, related_name='products', verbose_name='Категорії')
    slug = models.SlugField(unique=True)
    is_available = models.BooleanField(verbose_name='Наявність', default=True)
    is_active = models.BooleanField(verbose_name='Активність', default=False)
    created_at = models.DateTimeField(
        verbose_name='Дата створення', auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='Дата оновлення', auto_now=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукти'

    def get_add_to_cart_url(self):
        '''Function to get URL to add to cart'''

        return reverse_lazy('cart:add_to_cart', args=[self.slug])

    def get_absolute_url(self):
        return reverse_lazy('store:product', args=[self.slug])

    def __str__(self):
        return self.title


class SliderItem(models.Model):
    '''Model for saving slider images'''

    image = models.ImageField(
        verbose_name='Зображення', upload_to='slider_images/%Y/%m/%d/')
    is_active = models.BooleanField(verbose_name='Активність', default=False)
    created_at = models.DateTimeField(
        verbose_name='Дата створення', auto_now_add=True)

    def image_preview(self):
        return mark_safe(f'<img src="{self.image.url}" width="100" />')
    image_preview.short_description = 'Image'

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайди'

    def __str__(self):
        return f'{self.pk}'


class Store(models.Model):
    '''Point of sale'''

    adress = models.CharField(verbose_name='Адреса',
                              max_length=255, db_index=True)
    is_active = models.BooleanField(verbose_name='Активність', default=True)
    created_at = models.DateTimeField(
        verbose_name='Дата створення', auto_now_add=True)

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазини'

    def __str__(self):
        return self.adress


class Collection(models.Model):
    '''
    Basic model for creating collections
    with the ability to specify the order
    '''

    sequence_number = models.PositiveSmallIntegerField(
        verbose_name='Порядковий номер')
    is_active = models.BooleanField(verbose_name='Активність', default=True)
    updated_at = models.DateTimeField(
        verbose_name='Дата оновлення', auto_now=True)

    class Meta:
        abstract = True
        ordering = ('sequence_number',)


class Recommendation(Collection):
    '''Model for storing recommendations'''

    item = models.OneToOneField(
        Product, on_delete=models.CASCADE, verbose_name='Продукт')

    class Meta:
        verbose_name = 'Рекомендація'
        verbose_name_plural = 'Рекомендації'

    def __str__(self):
        return self.item.title


class PopularProduct(Collection):
    '''Model for storing popular products'''

    item = models.OneToOneField(
        Product, on_delete=models.CASCADE, verbose_name='Продукт')

    class Meta:
        verbose_name = 'Популярний продукт'
        verbose_name_plural = 'Популярні продукти'

    def __str__(self):
        return self.item.title


class PopularCategory(Collection):
    '''Model for storing popular categories'''

    item = models.OneToOneField(
        Category, on_delete=models.CASCADE, verbose_name='Категорія')

    class Meta:
        verbose_name = 'Популярна категорія'
        verbose_name_plural = 'Популярні категорії'

    def __str__(self):
        return self.item.title


class Order(models.Model):
    customer_name = models.CharField(
        verbose_name="Ім'я замовника", max_length=255)
    phone_number = PhoneNumberField(verbose_name='Номер телефону')
    email = models.EmailField()
    comment = models.TextField(
        verbose_name='Коментар', max_length=250, blank=True, null=True)
    is_active = models.BooleanField(verbose_name='Активність', default=True)
    created_at = models.DateTimeField(
        verbose_name='Дата замовлення', auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='Дата оновлення', auto_now=True)

    class Meta:
        abstract = True


class PickUpOrder(Order):
    store = models.OneToOneField(
        Store, on_delete=models.PROTECT, verbose_name='Магазин')


class DeliveryOrder(Order):
    street = models.CharField(verbose_name='Вулиця', max_length=255)
    house = models.CharField(verbose_name='Будинок', max_length=10)
    entrance = models.CharField(verbose_name="Під'їзд", max_length=10)
    floor = models.CharField(verbose_name='Поверх', max_length=5)
    flat = models.CharField(verbose_name='Квартири', max_length=5)
    recipient_name = models.CharField(
        verbose_name="Ім'я отримувача", max_length=255)
    recipient_phone_number = PhoneNumberField(
        verbose_name='Номер телефону отримувача')
    recipient_email = models.EmailField(verbose_name='Email отримувача')
