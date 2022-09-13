from .models import Cart
from .services import get_cart, get_item_or_bind_to_cart, increase_item_quantity


def add_to_cart(request, slug):
    cart = get_cart(request.user)
    item = get_item_or_bind_to_cart(cart, slug)
    if not item[1]:
        increase_item_quantity(item[0])


def remove_from_cart(request, slug):
    pass


def reduse_quantity_item(request, slug):
    pass
