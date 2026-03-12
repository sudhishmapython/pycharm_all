from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from demoapp.models import Student, Product, Employee
from demoapp.serializer import StudentSerializer, ProductSerializer, EmployeeSerializer

from rest_framework import generics


# Create your views here.


@api_view(['GET','POST'])
def index(request):

    if request.method== 'GET':
        data=Student.objects.all()
        serializer=StudentSerializer(data,many=True)
        return Response(serializer.data)
    if request.method== 'POST':
        serializer = StudentSerializer(data=request.data)
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
        snippet = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StudentSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)




class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request):
        snippets = Product.objects.all()
        serializer = ProductSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    pagination_class = PageNumberPagination
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name', 'place']
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'place']







# class LargeResultsSetPagination(PageNumberPagination):
#     page_size = 1000
#     page_size_query_param = 'page_size'
#     max_page_size = 10000


# class BillingRecordsView(generics.ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     pagination_class = LargeResultsSetPagination

