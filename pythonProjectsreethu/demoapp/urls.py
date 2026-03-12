from . import views
from django.urls import path

urlpatterns = [
    path('demo',views.fun1,name='functn1'),
    path('',views.add_form,name='add'),
]
