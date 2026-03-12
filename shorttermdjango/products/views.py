from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


# Create your views here.

# def index(request):
#     product = Product.objects.all()
#     return render(request, 'index.html', {'product': product})



def about(request):
    student = {
        'name': 'ABCD',
        'year': '2015',
        'status': False
    }
    return render(request, 'index.html', student)



    # student_details={'students':[
    #     {
    #             'name':'Anika',
    #             'year':'2015',
    #             'status':False
    #     },
    #     {
    #             'name':'Binika',
    #             'year':'2015',
    #             'status':False
    #     }
    #
    #
    # ]}
    # return render(request, 'index.html', student_details)




