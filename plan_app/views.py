from django.shortcuts import render

# Create your views here.
from .models import Plan
from .seriallizers import PlanSerializer,ClassTypeSerializer
from rest_framework import generics


# 获取学习计划全部数据
class PlabView(generics.ListAPIView):
    queryset=Plan.objects.all()
    serializer_class=PlanSerializer
    # 过滤关联外键 获取学习计划所对应的课程
    filterset_fields=['course']


from rest_framework import generics

from .models import ClassType


# 根据课程分类ID获取班级类型
class ClassTypeListView(generics.ListAPIView):
  queryset = ClassType.objects.all()
  serializer_class = ClassTypeSerializer
    #过滤关联外键 获取班级所对应的课程
  filterset_fields = ['course']


