from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.safestring import mark_safe


class Category(models.Model):
    '''Food category'''

    title = models.CharField(max_length=255, db_index=True)
    image = models.ImageField(upload_to='categories/%Y/%m/%d/')
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    '''Product on the menu'''

    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.PositiveIntegerField(
        blank=True, null=True, validators=[MaxValueValidator(100, message='The entered value exceeds the maximum allowable')])
    weight = models.PositiveSmallIntegerField(blank=True, null=True)
    volume = models.PositiveSmallIntegerField(blank=True, null=True)
    calories = models.PositiveSmallIntegerField()
    categories = models.ManyToManyField(Category, related_name='products')
    slug = models.SlugField(unique=True)
    is_available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class SliderItem(models.Model):
    '''Model for saving slider images'''

    image = models.ImageField(upload_to='slider_images/%Y/%m/%d/')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def image_preview(self):
        return mark_safe(f'<img src="{self.image.url}" width="100" />')
    image_preview.short_description = 'Image'

    def __str__(self):
        return f'{self.pk}'


class Store(models.Model):
    '''Point of sale'''

    adress = models.CharField(max_length=255, db_index=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.adress


class Collection(models.Model):
    '''
    Basic model for creating collections
    with the ability to specify the order
    '''

    sequence_number = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('sequence_number',)


class Recommendation(Collection):
    '''Model for storing recommendations'''

    item = models.OneToOneField(Product, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.item.title


class PopularCategory(Collection):
    '''Model for storing popular categories'''

    item = models.OneToOneField(Category, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = 'Popular categories'

    def __str__(self):
        return self.item.title
