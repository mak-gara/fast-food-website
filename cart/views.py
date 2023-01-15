from django.http import Http404
from django.shortcuts import redirect

from .services import check_item, get_cart, create_item_and_add_to_cart, get_cart_item_or_404, increase_item_quantity, decrease_item_quantity, remove_item_from_cart, set_item_quantity


def add_to_cart(request, slug):
    '''Додавання елемента в корзину'''

    cart = get_cart(request)
    item = check_item(cart, slug)
    if item:
        increase_item_quantity(item)
    else:
        create_item_and_add_to_cart(cart, slug)
    return redirect(request.META.get('HTTP_REFERER'))


def set_quantity_of_items(request, slug, quantity):
    '''Встановлення кількості для елементу корзини'''

    if quantity <= 0:
        raise Http404()
    cart = get_cart(request)
    item = check_item(cart, slug)
    if item:
        set_item_quantity(item, quantity)
    else:
        create_item_and_add_to_cart(cart, slug, quantity)
    return redirect(request.META.get('HTTP_REFERER'))


def remove_from_cart(request, slug):
    '''Видалення елементу з корзини'''

    cart = get_cart(request)
    item = get_cart_item_or_404(cart, slug)
    remove_item_from_cart(cart, item)
    return redirect(request.META.get('HTTP_REFERER'))


def reduse_quantity_item(request, slug):
    '''Зменшення кількості на 1 для елементу корзини'''

    cart = get_cart(request)
    item = get_cart_item_or_404(cart, slug)
    quantity = decrease_item_quantity(item)
    if quantity == 0:
        remove_item_from_cart(cart, item)
    return redirect(request.META.get('HTTP_REFERER'))
