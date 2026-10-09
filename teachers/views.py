from django.shortcuts import render
from .models import Teacher
from rest_framework import generics
from .serializers import TeacherSerializer
# Create your views here.



# 获取讲师所有列表
class TeacherView(generics.ListAPIView):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer
    
