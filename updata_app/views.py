from django.shortcuts import render

# Create your views here.


# 获取更新课程的所有数据并过滤出对应内容
from .models import UpdateCourse
from .serializers import UpdateSerializer
from rest_framework import generics


class UpateViews(generics.ListAPIView):
    # 更新公告列表为公开内容。
    authentication_classes = []

    queryset=UpdateCourse.objects.all().order_by('-create_time')
    serializer_class=UpdateSerializer

    filterset_fields = ['course','stage']



# 获取单个数据 url需要传递id

class UptateView(generics.RetrieveAPIView):
    # 更新公告详情为公开内容。
    authentication_classes = []

    queryset=UpdateCourse.objects.all()
    serializer_class=UpdateSerializer

