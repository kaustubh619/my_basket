# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categories(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='category_thumbnails/')

    def __str__(self):
        return str(self.title)


class Products(models.Model):

    class Meta:
        verbose_name_plural = 'Products'

    category = models.ForeignKey(Categories, on_delete=models.PROTECT)
    product_name = models.CharField(max_length=200)
    max_retail_price = models.IntegerField()
    discount = models.IntegerField()
    selling_price = models.IntegerField()
    images = models.TextField()

    def __str__(self):
        return str(self.product_name)


