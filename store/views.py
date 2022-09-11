from django.views.generic import TemplateView, ListView, DetailView

from store.models import Category

from .models import Product
from .services import get_active_category, get_active_category_by_slug, get_active_product_by_category, get_active_product_by_slug


class HomepageTemplateView(TemplateView):
    template_name = 'store/homepage.html'


class CategoryListView(ListView):
    template_name = 'store/categories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return get_active_category()


class DishListView(ListView):
    template_name = 'store/products.html'
    context_object_name = 'products'
    paginate_by = 9

    def get_queryset(self):
        category = get_active_category_by_slug(self.kwargs.get('slug'))
        return get_active_product_by_category(category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = get_active_category()
        return context


class DishDetailView(DetailView):
    template_name = 'store/product.html'
    context_object_name = 'product'

    def get_object(self):
        return get_active_product_by_slug(self.kwargs.get('slug'))
