from django.shortcuts import render
from rest_framework import generics
from .models import employee
from .serializers import EmployeeSerializer
from rest_framework.decorators import api_view


# Create your views here.


class emplist(generics.ListAPIView):
    queryset = employee.objects.all()
    serializer_class = EmployeeSerializer

class empcreate(generics.CreateAPIView):
    queryset = employee.objects.all()
    serializer_class = EmployeeSerializer

class empupdate(generics.RetrieveUpdateAPIView):
    queryset = employee.objects.all()
    serializer_class = EmployeeSerializer

class empdelete(generics.RetrieveDestroyAPIView):
    queryset = employee.objects.all()
    serializer_class = EmployeeSerializer