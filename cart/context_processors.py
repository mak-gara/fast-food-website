from .models import Cart
from .services import get_cart


def cart(request):
    return {
        'cart': get_cart(request)
    }
