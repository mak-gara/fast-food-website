from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView

from .forms import PickUpOrderForm, DeliveryOrderForm
from cart.services import get_cart
from .services import hide_cart


class PickUpOrderView(CreateView):
    template_name = 'store/pick-up-order.html'
    form_class = PickUpOrderForm
    success_url = reverse_lazy('store:home')

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


class EmptyCartView(TemplateView):
    template_name = 'orders/empty-cart.html'
