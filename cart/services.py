from django.db.models import F
from django.shortcuts import get_object_or_404
from django.http import Http404

from store.services import get_active_product_by_slug
from .models import Cart, CartItem


def get_cart_or_404(user):
    return get_object_or_404(Cart, user=user)


def get_cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.get_or_create(user=request.user)[0]
        return cart
    else:
        if not request.session.session_key:
            request.session.create()
        cart = Cart.objects.get_or_create(
            session_key=request.session.session_key)[0]
        return cart


def get_cart_item_or_404(cart, slug):
    items = cart.items.filter(product__slug=slug)
    if items.exists():
        return items[0]
    raise Http404()


def check_item(cart, slug):
    items = cart.items.filter(product__slug=slug, product__is_active=True)
    if items.exists():
        return items[0]


def create_item_and_add_to_cart(cart, slug):
    item = CartItem.objects.create(product=get_active_product_by_slug(slug))
    cart.items.add(item)


def increase_item_quantity(item):
    '''
    Function for incrementing the value
    of the qunatity field of the CartItem model
    '''
    item.quantity = F('quantity') + 1
    item.save()


def decrease_item_quantity(item):
    item.quantity = F('quantity') - 1
    item.save()
    item.refresh_from_db()
    return item.quantity


def remove_item_from_cart(cart, item):
    cart.items.remove(item)
