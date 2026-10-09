from .models import preson_app,UserSection
from rest_framework import serializers
from order_app.models import Order_app

class PresonSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(source="course.id")
    course_name=serializers.CharField(source="course.name")
    class Meta:
        model=preson_app
        fields="__all__"



class UserSectionSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(source="section.id")
    section_name=serializers.CharField(source="section.name")
    section_duration = serializers.CharField(source='section.duration')
    section_learn_count = serializers.CharField(source='section.learned_count')
    create_time=serializers.DateTimeField(format="%Y-%m")
    # 多写了唯一的课程小节  用户收藏课程小节是只能是一个小节只能收藏一次 也就是唯一的
    section = serializers.IntegerField(required=True)
    class Meta:
        model=UserSection
        fields="__all__"

# 获取订单列表
class OrderSerializers(serializers.ModelSerializer):
    # 额外获取课程名称 和班级名称
    course_name=serializers.CharField(source="course.name")
    classtype_name=serializers.CharField(source="classtype.name")
    class Meta:
        model=Order_app
        fields="__all__"