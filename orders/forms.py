from django import forms
from django.forms import ModelForm

from .models import PickUpOrder, DeliveryOrder, Order
from cart.services import get_cart
from store.services import get_active_stores


class PickUpOrderForm(ModelForm):
    PAYMENT_EMPTY = (('', 'Виберіть спосіб оплати'),)
    customer_name = forms.CharField(label='Ім\'я',
                                    widget=forms.TextInput(attrs={'placeholder': 'Андрій'}))
    phone_number = forms.CharField(label='Номер телефону',
                                   widget=forms.TextInput(attrs={'placeholder': '+380 99 xxx xx xx'}))
    email = forms.EmailField(label='Електронна адреса', widget=forms.TextInput(
        attrs={'placeholder': 'example@gmail.com'}))
    payment = forms.ChoiceField(
        label='Спосіб оплати', choices=PAYMENT_EMPTY+Order.PAYMENT)
    store = forms.ModelChoiceField(
        label='Магазин', empty_label='Виберіть заклад', queryset=get_active_stores())
    comment = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Залиште свій коментар'}), required=False)

    class Meta:
        model = PickUpOrder
        exclude = ('cart', 'is_active')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        order = super().save(commit=False)
        order.cart = get_cart(self.request)
        if commit:
            order.save()
        return order


class DeliveryOrderForm(ModelForm):
    class Meta:
        model = DeliveryOrder
        exclude = ('cart', 'is_active')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        order = super().save(commit=False)
        order.cart = get_cart(self.request)
        if commit:
            order.save()
        return order
