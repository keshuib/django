from rest_framework import serializers
from .models import Plan,ClassType
# 学习计划序列化
class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model=Plan
        fields="__all__"


# 班级序列化
class ClassTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClassType
        fields="__all__"
