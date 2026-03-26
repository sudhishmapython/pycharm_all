from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),

    path('add-template/', views.add_template, name='add_template'),
    path('generate/', views.generate_certificate, name='generate'),
    path('verify/', views.verify_certificate, name='verify'),
]