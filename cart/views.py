from django.views.generic import TemplateView
from django.shortcuts import redirect

from .services import get_cart, get_cart_by_session_key, get_cart_item_or_404, get_cart_or_404, get_item_or_bind_to_cart, increase_item_quantity


class CartPageTemplateView(TemplateView):
    template_name = 'cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            cart = get_cart_or_404(self.request.user)
        else:
            cart = get_cart_by_session_key(self.request.session.session_key)
        context['cart'] = cart
        context['cart_items'] = cart.items.all()
        return context


def add_to_cart(request, slug):
    if request.user.is_authenticated:
        cart = get_cart(request.user)
    else:
        cart = get_cart_by_session_key(request.session.session_key)
    item = get_item_or_bind_to_cart(cart, slug)
    if not item[1]:
        increase_item_quantity(item[0])
    return redirect('cart:cart')


def remove_from_cart(request, slug):
    cart = get_cart_or_404(request.user)
    item = get_cart_item_or_404(cart, slug)
    cart.items.remove(item)
    return redirect('cart:cart')


def reduse_quantity_item(request, slug):
    cart = get_cart_or_404(request.user)
    return redirect('cart:cart')
