from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import PickUpOrderForm, DeliveryOrderForm

class PickUpOrderView(CreateView):
    template_name = 'store/pick-up-order.html'
    form_class = PickUpOrderForm
    success_url = reverse_lazy('store:home')