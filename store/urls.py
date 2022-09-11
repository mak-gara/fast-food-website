from django.urls import path

from .views import CategoryListView, DishDetailView, DishListView, HomepageTemplateView


app_name = 'store'

urlpatterns = [
    path('', HomepageTemplateView.as_view(), name='home'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('products/<slug:slug>', DishListView.as_view(), name='products'),
    path('product/<slug:slug>', DishDetailView.as_view(), name='product'),
]