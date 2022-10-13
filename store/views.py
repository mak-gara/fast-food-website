from pipes import Template
from django.views.generic import TemplateView, ListView, DetailView

from .services import get_active_popular_categories, get_active_category, get_active_category_by_slug, get_active_product_by_slug, get_active_slides, get_active_recommendations, get_active_products_by_category


class HomepageTemplateView(TemplateView):
    template_name = 'store/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slides'] = get_active_slides()
        context['categories'] = get_active_popular_categories()
        context['recommendations'] = get_active_recommendations()
        return context


class CategoryListView(ListView):
    template_name = 'store/categories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return get_active_category()


class ProductListView(ListView):
    template_name = 'store/products.html'
    context_object_name = 'products'
    paginate_by = 6
    
    def get_queryset(self):
        self.active_category = get_active_category_by_slug(self.kwargs.get('slug'))
        products = get_active_products_by_category(self.active_category)
        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_category'] = self.active_category
        context['categories'] = get_active_category()
        return context


class ProductDetailView(DetailView):
    template_name = 'store/product.html'
    context_object_name = 'product'

    def get_object(self):
        return get_active_product_by_slug(self.kwargs.get('slug'))


class ContactsTemplateView(TemplateView):
    template_name = 'store/contacts.html'
