from . import views
from django.urls import path, include

urlpatterns = [
    path('temp',views.index,name="fun1"),
    path('',views.temppage,name='fun2')

]