from django.urls import path

from . import views

urlpatterns = [
    path('first',views.fun1,name='function1'),
    path('demo',views.fun2,name='funcion2'),
    path('demo1',views.index,name='index1'),
    path('', views.formdata, name='formdetails'),
    path('view',views.student_read,name='s_read'),
    path('s_update/<int:id>',views.sud_update,name='studupdates'),
    path('ureg', views.user_reg, name='u1'),
    # path('nreg', views.nurse_reg, name='n1'),

    ]