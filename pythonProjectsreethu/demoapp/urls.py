from . import views
from django.urls import path

urlpatterns = [
    path('demo',views.fun1,name='functn1'),
    path('',views.add_form,name='add'),
    path('p_read', views.read_form, name='read'),
    path('p_edit/<int:id>/', views.update_form, name='edit'),
]
