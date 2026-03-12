from . import views
from django.urls import path

urlpatterns = [

    path('demo',views.first,name='firstview'),
    path('demo1',views.second,name='secondview'),
    path('data',views.third,name='thirdview'),
    path('view', views.studview, name='studviews'),
    path('update/<int:id>', views.studupdate, name='studupdates'),
    # path('regs',views.reg,name='regstr'),
    path('',views.radiofun,name='rfun'),

]