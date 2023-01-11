from django.contrib import admin

from .models import PickUpOrder, DeliveryOrder


@admin.register(PickUpOrder)
class PickUpOrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer_name',
        'phone_number',
        'email',
        'store',
        'payment',
        'is_active',
        'created_at'
    )
    list_filter = (
        'created_at',
        'is_active'
    )
    list_editable = (
        'is_active',
    )


@admin.register(DeliveryOrder)
class DeliveryOrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer_name',
        'phone_number',
        'email',
        'recipient_name',
        'recipient_phone_number',
        'recipient_email',
        'street',
        'house',
        'entrance',
        'floor',
        'flat',
        'payment',
        'is_active',
        'created_at'
    )
    list_filter = (
        'created_at',
        'is_active'
    )
    list_editable = ('is_active',)
    readonly_fields = (
        'id',
        'created_at'
    )
    fieldsets = (
        ('Інформація про замовлення', {
            'fields': (('id', 'created_at'), 'is_active')
        }),
        ('Кошик', {'fields': ('cart',)}),
        ('Особисті дані', {
            'fields': (
                ('customer_name', 'phone_number', 'email'),
                ('recipient_name', 'recipient_phone_number', 'recipient_email'))
        }),
        ('Доставка', {
            'fields': ('street', 'house', 'entrance', 'floor', 'flat')
        }),
        ('Коментар', {
            'fields': ('comment',)
        }),
        ('Оплата', {
            'fields': ('payment',)
        })
    )
