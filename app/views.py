# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template

from rest_framework import viewsets, status
from rest_framework.response import Response


from .models import Categories
from .serializers import CategorySerializer

@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

# @login_required(login_url="/login/")
# def pages(request):
#     context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    # try:
        
    #     load_template      = request.path.split('/')[-1]
    #     context['segment'] = load_template
        
    #     html_template = loader.get_template( load_template )
    #     return HttpResponse(html_template.render(context, request))
        
    # except template.TemplateDoesNotExist:

    #     html_template = loader.get_template( 'page-404.html' )
    #     return HttpResponse(html_template.render(context, request))

    # except:
    
    #     html_template = loader.get_template( 'page-500.html' )
    #     return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def category(request):
    obj = Categories.objects.all()
    return render(request, 'category.html', {"categories": obj})


class AddCategory(viewsets.ViewSet):
    def category_list(self, request):
        queryset = Categories.objects.all()
        serializer = CategorySerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
