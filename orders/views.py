from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView

from .forms import PickUpOrderForm, DeliveryOrderForm
from cart.services import get_cart, hide_cart


class CreateOrderMixin:

    def get(self, request, *args, **kwargs):
        # перевірка чи непорожня корзина
        if get_cart(request).items.exists():
            return super().get(request, *args, **kwargs)
        return redirect('orders:empty_cart')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        response = super().form_valid(form)
        hide_cart(get_cart(self.request))
        return response


class PickUpOrderView(CreateOrderMixin, CreateView):
    template_name = 'orders/pick-up-order.html'
    form_class = PickUpOrderForm
    success_url = reverse_lazy('store:home')


class DeliveryOrderView(CreateOrderMixin, CreateView):
    template_name = 'orders/delivery-order.html'
    form_class = DeliveryOrderForm
    success_url = reverse_lazy('store:home')


class EmptyCartView(TemplateView):
    template_name = 'orders/empty-cart.html'
