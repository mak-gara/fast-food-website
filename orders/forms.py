from django import forms
from django.forms import ModelForm

from .models import PickUpOrder, DeliveryOrder, Order
from cart.services import get_cart
from store.services import get_active_stores


class OrderForm(ModelForm):
    PAYMENT_EMPTY = (('', 'Виберіть спосіб оплати'),)
    customer_name = forms.CharField(label='Ім\'я',
                                    widget=forms.TextInput(attrs={'placeholder': 'Андрій'}))
    phone_number = forms.CharField(label='Номер телефону',
                                   widget=forms.TextInput(attrs={'placeholder': '+380 99 xxx xx xx'}))
    email = forms.EmailField(label='Електронна адреса', widget=forms.EmailInput(
        attrs={'placeholder': 'example@gmail.com'}))
    payment = forms.ChoiceField(
        label='Спосіб оплати', choices=PAYMENT_EMPTY+Order.PAYMENT)
    comment = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Залиште свій коментар'}), required=False)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        order = super().save(commit=False)
        order.cart = get_cart(self.request)
        if commit:
            order.save()
        return order


class PickUpOrderForm(OrderForm, ModelForm):
    store = forms.ModelChoiceField(
        label='Магазин', empty_label='Виберіть заклад', queryset=get_active_stores())

    class Meta:
        model = PickUpOrder
        exclude = ('cart', 'is_active')


class DeliveryOrderForm(OrderForm, ModelForm):
    recipient_name = forms.CharField(label='Ім\'я отримувача', widget=forms.TextInput(
        attrs={'placeholder': 'Вікторія'}))
    recipient_phone_number = forms.CharField(label='Номер телефону отримувача', widget=forms.TextInput(
        attrs={'placeholder': '+380 99 xxx xx xx'}))
    recipient_email = forms.EmailField(label='Електронна адреса отримувача', widget=forms.EmailInput(
        attrs={'placeholder': 'example@gmail.com'}))
    street = forms.CharField(label='Вулиця', widget=forms.TextInput(
        attrs={'placeholder': 'вул. Степана Бандери'}))
    house = forms.CharField(label='Номер будинку',
                            widget=forms.TextInput(attrs={'placeholder': '12'}))
    entrance = forms.CharField(
        label='Номер під\'їзду', widget=forms.TextInput(attrs={'placeholder': '10'}), required=False)
    floor = forms.CharField(
        label='Номер поверху', widget=forms.TextInput(attrs={'placeholder': '3'}), required=False)
    flat = forms.CharField(
        label='Номер квартири', widget=forms.TextInput(attrs={'placeholder': '5'}), required=False
    )

    class Meta:
        model = DeliveryOrder
        exclude = ('cart', 'is_active')
