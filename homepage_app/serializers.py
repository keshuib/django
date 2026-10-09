from .models import RotationChart,FeatureService
from rest_framework import serializers
# 轮播序列化
class RoutationSerializers(serializers.ModelSerializer):
    class Meta:
        model=RotationChart
        fields="__all__"


# 特色服务序列化
class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model=FeatureService
        fields="__all__"