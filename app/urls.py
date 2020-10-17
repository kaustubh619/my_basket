# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('category', views.category, name='category'),
    path('product', views.product, name='product'),
    path('add_category', views.AddCategory.as_view({'get':'category_list'})),

    path('add_product_images', views.AddProductImages.as_view()),
    path('add_product', views.AddProduct.as_view({'get': 'product_list'})),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
