from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Certificate
from .serializer import CertificateSerializer


# Add Certificate
class CertificateCreate(APIView):
    def post(self, request):
        serializer = CertificateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# View All Certificates
class CertificateList(APIView):
    def get(self, request):
        certificates = Certificate.objects.all()
        serializer = CertificateSerializer(certificates, many=True)
        return Response(serializer.data)


# Verify Certificate
class VerifyCertificate(APIView):
    def put(self, request, pk):
        certificate = Certificate.objects.get(id=pk)
        certificate.status = "verified"
        certificate.save()
        return Response({"message": "Certificate Verified"})


# Pending Certificates
class PendingCertificates(APIView):
    def get(self, request):
        certificates = Certificate.objects.filter(status="pending")
        serializer = CertificateSerializer(certificates, many=True)
        return Response(serializer.data)