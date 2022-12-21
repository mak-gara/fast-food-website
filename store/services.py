from django.shortcuts import get_object_or_404, get_list_or_404
from random import randint

from .models import Category, PopularCategory, Product, Recommendation, SliderItem, PopularProduct


# Category model
def get_active_category():
    '''Function to get all active categories'''

    return Category.objects.filter(is_active=True)


def get_active_category_by_slug(slug):
    '''Function to get active category by slug'''

    return get_object_or_404(Category, slug=slug, is_active=True)


def get_active_categories(amount='all'):
    '''Function to get active categories'''

    categories = Category.objects.filter(is_active=True)
    if amount == 'all':
        return categories
    else:
        return categories[:amount]


# PopularCategory model
def get_active_popular_categories():
    '''Function to get active popular categories'''

    return PopularCategory.objects.filter(is_active=True, item__is_active=True)


# Recommendation model
def get_active_recommendations():
    '''Function to get active recommendations'''

    return Recommendation.objects.filter(is_active=True, item__is_active=True, item__categories__is_active=True).distinct()

def get_active_popular_products():
    '''Function to get popular products'''

    return PopularProduct.objects.filter(is_active=True, item__is_active=True, item__categories__is_active=True).distinct()

# Product model
def get_active_products():
    '''Function to get active products'''

    return Product.objects.filter(is_active=True, categories__is_active=True).distinct()


def get_active_product_by_slug(slug):
    '''Function to get active product by slug'''

    return get_list_or_404(Product, slug=slug, is_active=True, categories__is_active=True)[0]


def get_active_products_by_category(category):
    '''Function of obtaining active products in a certain category'''

    return category.products.filter(is_active=True, categories__is_active=True).distinct()


def get_random_product():
    '''
    Function of obtaining a random product
    from the list of all active products
    '''

    products = get_active_products()
    return products[randint(0, products.count() - 1)]


# SliderItem model
def get_active_slides(amount='all'):
    '''Function to get active slides'''

    slides = SliderItem.objects.filter(is_active=True)
    if amount == 'all':
        return slides
    else:
        return slides[:amount]
