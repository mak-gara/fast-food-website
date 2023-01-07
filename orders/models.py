from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from store.models import Store
from cart.models import Cart

class Order(models.Model):
    PAYMENT = (
        ('cash', 'Оплата готівкою'),
    )
    cart = models.OneToOneField(
        Cart, on_delete=models.PROTECT, verbose_name='Кошик')
    customer_name = models.CharField(
        verbose_name="Ім'я замовника", max_length=255)
    phone_number = PhoneNumberField(verbose_name='Номер телефону')
    email = models.EmailField()
    payment = models.CharField(
        verbose_name='Оплата', max_length=4, choices=PAYMENT)
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
    store = models.ForeignKey(
        Store, on_delete=models.PROTECT, verbose_name='Магазин')

    class Meta:
        verbose_name = 'Самовивіз'
        verbose_name_plural = 'Самовивіз'


class DeliveryOrder(Order):
    street = models.CharField(verbose_name='Вулиця', max_length=255)
    house = models.CharField(verbose_name='Будинок', max_length=10)
    entrance = models.CharField(
        verbose_name="Під'їзд", max_length=10, blank=True, null=True)
    floor = models.CharField(verbose_name='Поверх',
                             max_length=5, blank=True, null=True)
    flat = models.CharField(verbose_name='Квартира',
                            max_length=5, blank=True, null=True)
    recipient_name = models.CharField(
        verbose_name="Ім'я отримувача", max_length=255)
    recipient_phone_number = PhoneNumberField(
        verbose_name='Номер телефону отримувача')
    recipient_email = models.EmailField(verbose_name='Email отримувача')

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставка'
