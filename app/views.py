# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes


from .models import Categories, Products
from .serializers import CategorySerializer, ProductSerializer

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


@login_required(login_url="/login/")
def product(request):
    obj = Products.objects.all()
    categories = Categories.objects.all()
    return render(request, 'product.html', {"products": obj, "categories": categories})

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


def handle_uploaded_file(f):
    if not os.path.isdir("media/product_images/"):
        os.makedirs("media/product_images/")

    with open('media/product_images/' + f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
    return f.name


@permission_classes((AllowAny,))
class AddProductImages(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        res = {}
        for i in self.request.FILES:
            array = {}
            array['success'] = 1
            res['url'] = 'http://127.0.0.1:8000/media/product_images/' + handle_uploaded_file(self.request.FILES[i])
            array['file'] = res
        return Response(array)          


class AddProduct(viewsets.ViewSet):
    def product_list(self, request):
        queryset = Products.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)