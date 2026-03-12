from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from restapp.models import Category
from restapp.serializer import CategorySerializer


# Create your views here.

@api_view(['GET','POST'])
def add_category(request):

    if request.method== 'GET':
        data=Category.objects.all()
        serializer=CategorySerializer(data,many=True)
        return Response(serializer.data)
    if request.method== 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def demo_details(request,id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CategorySerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


# @api_view(['GET','POST'])
# def add_cake(request):
#
#     if request.method== 'GET':
#         data=Category.objects.all()
#         serializer=CategorySerializer(data,many=True)
#         return Response(serializer.data)
#     if request.method== 'POST':
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# @api_view(['GET','PUT','DELETE'])
# def cake_details(request,id):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Category.objects.get(id=id)
#     except Category.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = CategorySerializer(snippet)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = CategorySerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)
#
