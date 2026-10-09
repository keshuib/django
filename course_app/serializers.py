# 序列化
from rest_framework import serializers
from .models import Course,Stage,Chapter,Section


'''
外键序列化得到的只是id 数字 想要其他内容想要额外添加序列化

'''
class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        # 加上统计的字段的序列化 额外添加字段时 read_only=True不允许用户修改
        stage_count=serializers.IntegerField(read_only=True)
        chapter_coun=serializers.IntegerField(read_only=True)
        section_count=serializers.IntegerField(read_only=True)
        # 指定要序列的类
        model=Course
        # 指定要序列的字段
        fields='__all__'

# 阶段
class StageSerializers(serializers.ModelSerializer):
    class Meta:
        model=Stage
        fields="__all__"

# 章节
class ChapterSerializers(serializers.ModelSerializer):
    class Meta:
        model=Chapter
        fields="__all__"

# 小节
class SectionSerializers(serializers.ModelSerializer):
    class Meta:
        model=Section
        fields='__all__'
        



# 选中分类之后要求有对应的课程阶段
# class CourseDataSerializers(serializers.ModelSerializer):
#     stage=StageSerializers(many=True,read_only=True)
#     class Meta:
#           # 指定要序列的类
#         model=Course
#         # 指定要序列的字段
#         fields='__all__'


# 选中阶段之后要有课程章节
# class StageDateSerializers(serializers.ModelSerializer):
#      chapter=ChapterSerializers(many=True,read_only=True)
#      class Meta:
#         model=Stage
#         fields="__all__"



# 选中章节之后要有节
class SectionDataSerializers(serializers.ModelSerializer):
    sction=SectionSerializers(many=True,read_only=True)
    class Meta:
        model=Chapter
        fields="__all__"


# 选中阶段之后既有章节也有小节
class StageDateSerializers(serializers.ModelSerializer):
     chapter=SectionDataSerializers(many=True,read_only=True)
     class Meta:
        model=Stage
        fields="__all__"


# 选中分类之后全都要
class DateAllSerializers(serializers.ModelSerializer):
    stage=StageDateSerializers(many=True,read_only=True)
    class Meta:
          # 指定要序列的类
        model=Course
        # 指定要序列的字段
        fields='__all__'
# 序列化只能序列化他所有的 在嵌套时i必须是反向查询的字段名   