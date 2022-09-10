from django.db import models
from django.conf import settings

from store.models import Product


class CartItem(models.Model):
    '''Shopping cart element'''
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def get_total_item_price(self):
        return self.quantity * self.product.price
    
    def get_discount_item_price(self):
        return self.quantity * self.product.discount_price
    
    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_discount_item_price()
    
    def get_final_price(self):
        if self.product.discount_price:
            return self.get_discount_item_price()
        return self.get_total_item_price()
    
    def __str__(self):
        return f'{self.product.title} - {self.quantity}'


class Cart(models.Model):
    '''Shopping cart model'''
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    created_at = models.DateTimeField(auto_now_add=True)
    ordered_at = models.DateTimeField()
    is_ordered = models.BooleanField(default=False)

    def get_total_price(self):
        return sum([i.get_final_price() for i in self.items.all()])
    
    def __str__(self):
        return self.user.username
