from rest_framework import serializers
from .models import FreeCourse
class FreeCourseSerializer(serializers.ModelSerializer):
    # 额外追加 时间格式化 以及 课程名称 和讲师名称字段序列化 read_only=True不允许用户修改 
    stage_name=serializers.CharField(source="stage_name",read_only=True)
    teacher_name=serializers.CharField(source="teacher_name",read_only=True)
    start_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    end_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model=FreeCourse
        fields="__all__"