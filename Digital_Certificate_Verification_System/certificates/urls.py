from . import views
from django.urls import path


urlpatterns = [

    path('', views.generate_certificate, name='generate'),
    path('verify/',views.verify_certificate, name='verify'),
]