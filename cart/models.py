from django.db import models
from django.conf import settings

from store.models import Product


class CartItem(models.Model):
    '''Shopping cart element'''

    is_ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.product.title} - {self.quantity}'

    def get_total_product_price(self):
        '''
        Function calculation of the total price
        of products of the same type
        '''
        return self.quantity * self.product.price

    def get_discount_product_price(self):
        '''
        Function for calculating the total
        savings amount of products of the same type
        '''
        if self.product.discount_percentage:
            discount_price = self.product.price * \
                self.product.discount_percentage / 100 * self.quantity
            return round(discount_price, 2)

    def get_final_price(self):
        '''
        Function for calculating the final price.
        With discount or without
        '''
        total_price = self.get_total_product_price()
        discount_price = self.get_discount_product_price()
        if discount_price:
            return total_price - discount_price
        return total_price


class Cart(models.Model):
    '''Shopping cart model'''

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    ordered_at = models.DateTimeField(blank=True, null=True)
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total_price(self):
        '''
        Function to calculate the total cost
        of all products in the basket
        '''
        prices = [item.get_final_price() for item in self.items.all()]
        return sum(prices)
