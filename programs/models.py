from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """ A model to handle Program Categories """
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254, null=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class Programs(models.Model):
    """ A model to handle program post, presented as blog posts """

    class Meta:
        verbose_name_plural = "Programs"

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    is_free = models.BooleanField(default=False)
    title = models.CharField(max_length=254, null=True, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.title