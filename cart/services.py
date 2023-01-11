from django.db.models import F
from django.shortcuts import get_object_or_404
from django.http import Http404

from store.services import get_active_product_by_slug
from .models import Cart, CartItem


def get_cart(request):
    '''
    Function to receive the cart of an authorized
    or anonymous user. If the cart does not exist,
    it will be created
    '''

    if request.user.is_authenticated:
        cart = Cart.objects.get_or_create(
            user=request.user, is_ordered=False)[0]
        return cart
    else:
        if not request.session.session_key:
            request.session.create()
        cart = Cart.objects.get_or_create(
            session_key=request.session.session_key, is_ordered=False)[0]
        return cart


def get_cart_or_404(user):
    '''
    Function to receive the cart. If the cart does not exist,
    a Http404() exception will be thrown
    '''

    return get_object_or_404(Cart, user=user)


def get_cart_item_or_404(cart, slug):
    '''
    Function to receive the cart item. If the cart item doesn't
    exist, a Http404() exeption will be thrown
    '''

    items = cart.items.filter(product__slug=slug)
    if items.exists():
        return items[0]
    raise Http404()


def check_item(cart, slug):
    '''Function to check if item is in cart'''

    items = cart.items.filter(product__slug=slug, product__is_active=True)
    if items.exists():
        return items[0]


def create_item_and_add_to_cart(cart, slug, quantity=1):
    '''Function to instantiate a CartItem and bind to cart'''

    item = CartItem.objects.create(
        product=get_active_product_by_slug(slug), quantity=quantity)
    cart.items.add(item)


def increase_item_quantity(item, quantity=1):
    '''
    Function to increase the value of the quantity
    field of the CartItem object by a given value
    '''

    item.quantity = F('quantity') + quantity
    item.save()
    item.refresh_from_db()
    return item.quantity


def decrease_item_quantity(item, quantity=1):
    '''
    Function to decrease the value of the quantity
    field of the CartItem object by a given value
    '''

    item.quantity = F('quantity') - quantity
    item.save()
    item.refresh_from_db()
    return item.quantity


def set_item_quantity(item, quantity):
    '''
    Function to set the value of the quantity
    field of CartItem object by given value
    '''

    item.quantity = quantity
    item.save()
    return item.quantity


def remove_item_from_cart(cart, item):
    '''
    Function to remove the link between the
    cart and the cart item, then delete
    the cart item from the database
    '''

    cart.items.remove(item)
    item.delete()


def hide_cart(cart):
    '''Function of hiding the cart'''

    cart.is_ordered = True
    cart.save()
