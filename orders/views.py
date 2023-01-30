from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import CreateView, TemplateView
from django.http import HttpRequest

from .forms import PickUpOrderForm, DeliveryOrderForm
from cart.services import get_cart, hide_cart


class CreateOrderMixin:
    def get(self, request, *args, **kwargs):
        if get_cart(request).items.exists():
            return super().get(request, *args, **kwargs)
        return redirect('orders:empty_cart')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        order = form.save()
        hide_cart(get_cart(self.request))
        return render(self.request, 'orders/order-info.html', {'order': order})


class PickUpOrderView(CreateOrderMixin, CreateView):
    template_name = 'orders/pick-up-order.html'
    form_class = PickUpOrderForm


class DeliveryOrderView(CreateOrderMixin, CreateView):
    template_name = 'orders/delivery-order.html'
    form_class = DeliveryOrderForm


class EmptyCartView(TemplateView):
    template_name = 'orders/empty-cart.html'
