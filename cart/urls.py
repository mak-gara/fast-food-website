from django.urls import path

from .views import add_to_cart, remove_from_cart, reduse_quantity_item, CartPageTemplateView

app_name = 'cart'

urlpatterns = [
    path('', CartPageTemplateView.as_view(), name='cart'),
    path('add/<slug:slug>/', add_to_cart, name='add_to_cart'),
    path('remove/<slug:slug>/', remove_from_cart, name='remove_from_cart'),
    path('reduce/<slug:slug>/', reduse_quantity_item, name='requse_quantity')
]