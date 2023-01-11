from django.contrib import admin

from .models import Cart, CartItem

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'quantity'
    )

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'session_key',
        'created_at',
        'ordered_at',
        'is_ordered'
    )
    list_editable = ('is_ordered',)

