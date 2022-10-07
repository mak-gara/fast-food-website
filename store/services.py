from django.shortcuts import get_object_or_404

from .models import Category, PopularCategory, Product, Recommendation, SliderItem


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


def get_active_categories(amount='all'):
    '''Function to get active categories'''

    categories = Category.objects.filter(is_active=True)
    if amount == 'all':
        return categories
    else:
        return categories[:amount]


# PopularCategory model
def get_active_popular_categories():
    return PopularCategory.objects.filter(is_active=True)


# Recommendation model
def get_active_recommendations():
    return Recommendation.objects.filter(is_active=True)


# Product model
def get_active_product_by_slug(slug):
    '''Function to get active product by slug'''

    return get_object_or_404(Product, slug=slug, is_active=True)


# SliderItem model
def get_active_slides(amount='all'):
    '''Function to get active slides'''

    slides = SliderItem.objects.filter(is_active=True)
    if amount == 'all':
        return slides
    else:
        return slides[:amount]
