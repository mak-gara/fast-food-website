from django.urls import path

from .views import PickUpOrderView, EmptyCartView


app_name = 'orders'

urlpatterns = [
    path('pick_up_order/', PickUpOrderView.as_view(), name='pick-up-order'),
    path('empty_cart/', EmptyCartView.as_view(), name='empty_cart')
]
