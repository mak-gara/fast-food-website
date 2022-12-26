from django.forms import ModelForm

from .models import PickUpOrder, DeliveryOrder
from cart.services import get_cart


class PickUpOrderForm(ModelForm):
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
