from django.db.models import F
from django.shortcuts import get_object_or_404

from store.services import get_active_product_by_slug
from .models import Cart, CartItem


def get_cart_or_404(user):
    return get_object_or_404(Cart, user=user)


def get_cart(user):
    '''
    Function to get the user's cart or
    if it doesn't exist - create
    '''
    cart = Cart.objects.get_or_create(user=user)
    return cart[0]

def get_cart_by_session_key(session_key):
    cart = Cart.objects.get_or_create(session_key=session_key)
    return cart[0]

def get_cart_item_or_404(cart, slug):
    items = cart.items.filter(product__slug=slug)
    if items.exists():
        return items[0]


def get_item_or_bind_to_cart(cart, slug):
    '''
    Function for getting an item from the cart,
    if such an item does not exist,
    then it is created and bound to the user's cart
    '''
    item = cart.items.filter(product__slug=slug)
    if item.exists():
        return (item[0], False)
    item = CartItem.objects.create(product=get_active_product_by_slug(slug))
    cart.items.add(item)
    return (item, True)


def increase_item_quantity(item):
    '''
    Function for incrementing the value
    of the qunatity field of the CartItem model
    '''
    item.quantity = F('quantity') + 1
    item.save()
