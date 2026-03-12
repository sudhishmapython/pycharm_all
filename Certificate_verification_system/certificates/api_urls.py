from django.urls import path
from .views import *

urlpatterns = [

    path('add-certificate/', CertificateCreate.as_view()),

    path('certificates/', CertificateList.as_view()),

    path('verify/<int:pk>/', VerifyCertificate.as_view()),

    path('pending/', PendingCertificates.as_view()),
]