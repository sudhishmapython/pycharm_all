from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),

    path('add-template/', views.add_template, name='add_template'),
    path('generate/', views.generate_certificate, name='generate'),
    path('verify/', views.verify_certificate, name='verify'),
    path('preview/', views.preview_certificate, name='preview_certificate'),
    path('preview-pdf/', views.preview_pdf, name='preview_pdf'),
    path('confirm/', views.confirm_certificate, name='confirm_certificate'),
]