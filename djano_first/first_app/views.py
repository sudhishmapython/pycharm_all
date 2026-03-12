from django.shortcuts import render, redirect
from django.http import HttpResponse
from first_app.models import Student, Product, Image
from .form import StudentForm, ProductForm, ImagesForm


# Create your views here.

# def index(request):
#     # return HttpResponse("welcome")
#     return render(request,'index1.html')

def index(request):
    student = {
        'name': 'futura',
        'year': '2015',
        'status': False
    }
    print(student)
    return render(request, 'index1.html', student)


# def index(request):
#     student_details={'students':[
#     {
#             'name':'Anika',
#             'year':'2015',
#             'status':True
#     },
#     {
#             'name':'Binika',
#             'year':'2016',
#             'status':False
#     }
#     ]}
#     return render(request, 'index1.html', student_details)


# def index(request):
#     return render(request, 'index.html')
#
#
def demo(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_view')

    return render(request, 'demo.html', {'form': form})


def student_view(request):
    Studentdetails = Student.objects.all()
    return render(request, "student_view.html", {'image': Studentdetails})


def student_update(request, up):
    studupdate = Student.objects.get(id=up)
    if request.method == 'POST':
        updateForm = StudentForm(request.POST, request.FILES, instance=studupdate)
        if updateForm.is_valid():
            updateForm.save()
            return redirect("student_view")
    else:
        updateForm = StudentForm(instance=studupdate)
    return render(request, "student_update.html", {'updateform': updateForm})


def student_delete(request, dl):
    studdelete = Student.objects.get(id=dl)
    studdelete.delete()
    return redirect("student_view")




def add(request):
    form=ProductForm()
    if request.method == 'POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view')

    return render(request,'form1.html',{'form':form})



def product_view(request):
    data=Product.objects.all()
    return  render(request,'view.html',{'data':data})


def product_edit(request,id):
    data=Product.objects.get(id=id)
    if request.method == 'POST':
        form=ProductForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect("view")
    else:
        form = ProductForm(instance=data)
    return render(request, 'edit.html',{'form':form})


def product_delete(request,id):
    data=Product.objects.get(id=id)
    data.delete()
    return redirect("view"  )



def fileupload(request):
    form = ImagesForm(request.POST, request.FILES)
    if request.method == 'POST':
        images = request.FILES.getlist('pic')
        for image in images:
            image_ins = Image(pic = image)
            image_ins.save()
        return redirect('index')
    context = {'form': form}
    return render(request, "upload.html", context)


def upload_view(request):
    data=Image.objects.all()
    return  render(request,'upload_view.html',{'data':data})