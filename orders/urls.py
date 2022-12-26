from django.urls import path

from .views import PickUpOrderView, EmptyCartView, DeliveryOrderView


app_name = 'orders'

urlpatterns = [
    path('delivery_order/', DeliveryOrderView.as_view(), name='delivery_order'),
    path('pick_up_order/', PickUpOrderView.as_view(), name='pick_up_order'),
    path('empty_cart/', EmptyCartView.as_view(), name='empty_cart')
]
