from django.contrib import admin
from .models import Category, Product, SliderItem, Store, Recommendation, PopularCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'created_at',
        'is_active'
    ]
    list_display_links = ['title']
    list_editable = ['is_active']
    search_fields = ['title']
    list_filter = ['is_active']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'price',
        'discount_percentage',
        'is_available',
        'is_active',
        'created_at',
        'updated_at'
    ]
    list_display_links = ['title']
    list_editable = [
        'is_available',
        'is_active'
    ]
    search_fields = ['title']
    autocomplete_fields = ['categories']
    list_filter = [
        'categories',
        'is_active',
        'is_available'
    ]


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'item',
        'sequence_number',
        'updated_at'
    ]
    list_display_links = ['item']
    list_editable = ['sequence_number']
    autocomplete_fields = ['item']
    list_filter = ['is_active']


@admin.register(PopularCategory)
class PopularCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'item',
        'sequence_number',
        'updated_at'
    ]
    list_display_links = ['item']
    list_editable = ['sequence_number']
    autocomplete_fields = ['item']
    list_filter = ['is_active']


@admin.register(SliderItem)
class SliderItemAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'image_preview',
        'is_active',
        'created_at'
    ]


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'adress',
        'is_active',
        'created_at'
    ]
    list_filter = ['is_active']
    list_editable = ['is_active']
