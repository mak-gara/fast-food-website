from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import PickUpOrderForm, DeliveryOrderForm
from cart.services import get_cart
from .services import hide_cart


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
        data = form.cleaned_data
        recipients = [data.get('email')]
        if data.get('recipient_email'):
            if data.get('email') != data.get('recipient_email'):
                recipients.append(data.get('recipient_email'))
        context = {
            'order_type': '',
            'data': data
        }
        subject = render_to_string('email/orders/order_letter_subject.txt', context)
        body = render_to_string('email/orders/order_letter_body.txt', context)
        send_mail(
            subject,
            body,
            'test@gmail.com',
            recipients
        )
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


class EmptyCartView(CreateOrderMixin, TemplateView):
    template_name = 'orders/empty-cart.html'
