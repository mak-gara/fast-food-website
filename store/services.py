from django.shortcuts import get_object_or_404

from .models import Category, Product

# Category model
def get_active_category():
    '''Function to get all active categories'''
    
    return Category.objects.filter(is_active=True)


def get_active_category_by_slug(slug):
    '''Function to get active category by slug'''
    
    return get_object_or_404(Category, slug=slug, is_active=True)


def get_active_product_by_category(category):
    '''Function to receive active products by category'''
    
    return category.products.filter(is_active=True)


# Product model
def get_active_product_by_slug(slug):
    '''Function to get active product by slug'''
    
    return get_object_or_404(Product, slug=slug, is_active=True)
