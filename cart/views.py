from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.http import Http404

from .services import check_item, get_cart, create_item_and_add_to_cart, get_cart_item_or_404, get_cart_or_404, increase_item_quantity, decrease_item_quantity, remove_item_from_cart, set_item_quantity


class CartPageTemplateView(TemplateView):
    template_name = 'cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = get_cart(self.request)
        context['cart'] = cart
        context['cart_items'] = cart.items.all()
        return context


def add_to_cart(request, slug):
    cart = get_cart(request)
    item = check_item(cart, slug)
    if item:
        increase_item_quantity(item)
    else:
        create_item_and_add_to_cart(cart, slug)
    return redirect('cart:cart')


def set_quantity_of_items(request, slug, quantity):
    if quantity <= 0:
        raise Http404()
    cart = get_cart(request)
    item = check_item(cart, slug)
    if item:
        set_item_quantity(item, quantity)
    else:
        create_item_and_add_to_cart(cart, slug, quantity)
    return redirect('cart:cart')


def remove_from_cart(request, slug):
    cart = get_cart_or_404(request.user)
    item = get_cart_item_or_404(cart, slug)
    remove_item_from_cart(cart, item)
    return redirect('cart:cart')


def reduse_quantity_item(request, slug):
    cart = get_cart_or_404(request.user)
    item = get_cart_item_or_404(cart, slug)
    quantity = decrease_item_quantity(item)
    if quantity == 0:
        remove_item_from_cart(cart, item)
    return redirect('cart:cart')
