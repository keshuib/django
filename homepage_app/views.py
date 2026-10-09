from django.shortcuts import render

# Create your views here.

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


from .serializers import RoutationSerializers,FeatureSerializer
from .models import RotationChart,FeatureService
from rest_framework import generics

# 视图缓存 轮播页面和特色服务 视图缓存需要借助method_decorator
@method_decorator(

    cache_page(60*60,cache="default",key_prefix="rotation_chart"),
    name="dispatch"
)
# 获取所有轮播数据 按从小到大排序
class RoutationCharView(generics.ListAPIView):
    queryset=RotationChart.objects.all().order_by("-id")
    serializer_class=RoutationSerializers

# 获取特色服务数据 并排序


@method_decorator(
    cache_page(60*60,cache="default",key_prefix="fearure_chart"),
    name="dispatch")
class FeatureView(generics.ListAPIView):
    queryset=FeatureService.objects.all().order_by("-id")
    serializer_class=FeatureSerializer
