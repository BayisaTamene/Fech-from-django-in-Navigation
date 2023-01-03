from django.shortcuts import render
from rest_framework import generics
from .models import student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view


# Create your views here.

# students crud operations

class studlist(generics.ListAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

class studcreate(generics.CreateAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

class studupdate(generics.RetrieveUpdateAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

class studdelete(generics.RetrieveDestroyAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer