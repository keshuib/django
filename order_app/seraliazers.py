from rest_framework import serializers
from .models import Order_app


# 创建获取订单序列化
class OrderAppSeralizer(serializers.ModelSerializer):
    # 序列化用户名称
    user_name=serializers.CharField(source="user.name")
    # 旧写法保留：Order_app 模型字段实际名为 coursr。
    # course_app=serializers.CharField(source="course.name")
    course_app=serializers.CharField(source="coursr.name", read_only=True)
    classtype_name=serializers.CharField(source="classtype.name")
    class Meta:
        model=Order_app
        fields="__all__"
