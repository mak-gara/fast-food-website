from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView

from .forms import PickUpOrderForm, DeliveryOrderForm
from cart.services import get_cart

class PickUpOrderView(CreateView):
    template_name = 'store/pick-up-order.html'
    form_class = PickUpOrderForm
    success_url = reverse_lazy('store:home')

    def get(self, request, *args, **kwargs):
        # перевірка чи непорожня корзина
        if get_cart(request).items.exists():
            return super().get(request, *args, **kwargs)
        return redirect('orders:empty_cart')

class EmptyCartView(TemplateView):
    template_name = 'orders/empty-cart.html'