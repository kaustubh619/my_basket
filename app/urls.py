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
    path('add_category', views.AddCategory.as_view({'get':'category_list'})),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
