from django.shortcuts import render
from rest_framework import generics
from .models import teacher
from .serializers import TeacherSerializer
from rest_framework.decorators import api_view


# Create your views here.

# students crud operations

class teachlist(generics.ListAPIView):
    queryset = teacher.objects.all()
    serializer_class = TeacherSerializer

class teachcreate(generics.CreateAPIView):
    queryset = teacher.objects.all()
    serializer_class = TeacherSerializer

class teachupdate(generics.RetrieveUpdateAPIView):
    queryset = teacher.objects.all()
    serializer_class = TeacherSerializer
class teachdelete(generics.RetrieveDestroyAPIView):
    queryset = teacher.objects.all()
    serializer_class = TeacherSerializer