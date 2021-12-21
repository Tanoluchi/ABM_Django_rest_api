from django.db.models import manager
from django.shortcuts import render
from rest_framework import serializers

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ProductSerializer
from .models import Product

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list',
        'Detail View': '/product-detail/<int:id>',
        'Create': '/product-create',
        'Update': '/product-update/<int:id>',
        'Delete': '/product-detail/<int:id>',
    }

    return Response(api_urls)

@api_view(['GET'])
def showAll(request):
    products = Product.objects.all()
    serializer_class = ProductSerializer(products, many=True)

    return Response(serializer_class.data)

@api_view(['GET'])
def viewProduct(request, id):
    product = Product.objects.get(id=id)
    serializer_class = ProductSerializer(product, many=False)

    return Response(serializer_class.data)

@api_view(['POST'])
def createProduct(request):
    serializer_class = ProductSerializer(data=request.data)

    if serializer_class.is_valid():
        serializer_class.save()

    return Response(serializer_class.data)

@api_view(['PUT'])
def updateProduct(request, id):
    product = Product.objects.get(id=id)
    serializer_class = ProductSerializer(instance=product, data=request.data)

    if serializer_class.is_valid():
        serializer_class.save()

    return Response(serializer_class.data)

@api_view(['DELETE'])
def deleteProduct(request, id):
    product = Product.objects.get(id=id)
    product.delete()

    return Response('Item delete successfully!')

