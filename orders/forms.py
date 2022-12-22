from django.forms import ModelForm

from .models import PickUpOrder, DeliveryOrder


class PickUpOrderForm(ModelForm):
    class Meta:
        model = PickUpOrder
        exclude = ('cart', 'is_active')


class DeliveryOrderForm(ModelForm):
    class Meta:
        model = DeliveryOrder
        exclude = ('cart', 'is_active')