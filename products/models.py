from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254, null=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Producer(models.Model):
    name = models.CharField(max_length=254, null=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.friendly_name


class Brand(models.Model):
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    producer = models.ForeignKey(
        'Producer',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    name = models.CharField(max_length=254, null=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    spec = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        return self.friendly_name


class Product(models.Model):
    brand = models.ForeignKey(
        'Brand',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    name = models.CharField(max_length=254, null=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    stock = models.PositiveSmallIntegerField(blank=True, null=True, default=5)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    thumbnail = models.BooleanField(default=False)

    def __str__(self):
        return self.friendly_name
