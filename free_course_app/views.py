from django.shortcuts import render
from rest_framework import generics
from .serializers import FreeCourseSerializer
from .models import FreeCourse
# Create your views here.

# 获取所有限免课程内容
class FreeCourseView(generics.ListAPIView):
    queryset=FreeCourse.objects.all()
    serializer_class=FreeCourseSerializer
    # 过滤关联的外键 只获取对应的内容 (限免课程所对应的阶段和讲师)
    filterset_fields =['stage','teacher']

    
    