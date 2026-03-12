from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from staticapp.forms import Customerform,Physicianform
# Create your views here.

def index(request):
    return render(request,'index.html')



def admin_page(request):
    return render(request, 'admindashboard.html')



def physician_page(request):
    return render(request, 'physiciandashboard.html')



def customer_page(request):
    return render(request, 'customerdashboard.html')

# def cust_reg(request):
#     form = Customerform()
#     if request.method=='POST':
#         form=Customerform(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('cust_reg')
#     return render(request,'customer_reg.html',{'form':form})


# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('uname')
#         password = request.POST.get('pass')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # messages.success(request, 'success')
#             return redirect('customer_page')
#         # else:
#         #     messages.success(request,'INVALID CREDENTIALS')
#     return render(request, 'login.html')
#

def logout_view(request):
    logout(request)
    return redirect('index')

def cust_reg(request):
    # print('working1')
    form=Customerform()
    if request.method=='POST':
        form=Customerform(request.POST,request.FILES)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_customer=True
            user.save()
            # messages.success(request, 'success')
            # print('submit1')
            return redirect('login')
    return render(request,'customer_reg.html',{'form':form})

def physician_reg(request):
    form=Physicianform()
    if request.method=='POST':
        form=Physicianform(request.POST)
        # print(form)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_physician=True
            user.save()
            # print('submit')
        return redirect('physician_reg')
    return render(request,'physician_reg.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_page')
            elif user.is_customer:
                return redirect('customer_page')
            elif user.is_physician:
                return redirect('physician_page')

        # else:
        #     messages.error(request, 'INVALID CREDENTIALS')
    return render(request, 'login.html')