from django.db.models import F

from store.services import get_active_product_by_slug
from .models import Cart, CartItem


def get_cart(user):
    '''
    Function to get the user's cart or
    if it doesn't exist - create
    '''
    cart = Cart.objects.get_or_create(user=user)
    return cart[0]


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