from django.urls import path

from .views import PickUpOrderView


app_name = 'orders'

urlpatterns = [
    path('pick-up-order/', PickUpOrderView.as_view(), name='pick-up-order'),
]
