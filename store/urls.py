from django.urls import path

from .views import AboutUsTemplateView, CategoryListView, ContactsTemplateView, DeliveryAndPaymentTemplateView, ProductDetailView, ProductListView, HomepageTemplateView, RandomProductDetailView


app_name = 'store'

urlpatterns = [
    path('', HomepageTemplateView.as_view(), name='home'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('products/<slug:slug>', ProductListView.as_view(), name='products'),
    path('product/<slug:slug>', ProductDetailView.as_view(), name='product'),
    path('random_product/', RandomProductDetailView.as_view(), name='random_product'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('about_us/', AboutUsTemplateView.as_view(), name='about_us'),
    path('delivery_and_payment/', DeliveryAndPaymentTemplateView.as_view(),
         name='delivery_and_payment'),
]
