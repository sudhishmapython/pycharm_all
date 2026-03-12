from rest_framework import serializers
from .models import Student, Product, Employee


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','place']



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =Product
        fields=['name','price','discription']




class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model =Employee
        fields=['name','job','salary']