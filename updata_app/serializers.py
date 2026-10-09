from .models import UpdateCourse
from rest_framework import serializers

class UpdateSerializer(serializers.ModelSerializer):
 
    # 额外获取阶段名称序列化
    course_name=serializers.CharField(source='couser.name',read_only=True)


    # 额外获取课程名称序列化
    stage_name=serializers.CharField(source="stage.name",read_only=True)

       # 获取时间格式化后的序列

    create_time = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model=UpdateCourse
        fields="__all__"