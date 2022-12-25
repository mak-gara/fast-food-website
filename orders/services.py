def hide_cart(cart):
    '''Function of hiding the cart'''

    cart.is_ordered = True
    cart.save()