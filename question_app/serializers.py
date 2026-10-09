from rest_framework import serializers
from .models import Question_app
from course_app.models import Section

# 提交问题序列化
class QuestionSeralizer(serializers.ModelSerializer):
        model=Question_app
        fields="__all__"
        # 关联外籍只序列化id 那么在去写接口获取时 也只有id 如果要具体内容 需要额外添加序列化


# 回答问题序列化
class AnswerAddSerializer(serializers.ModelSerializer):
    # 回答内容
    content = serializers.CharField(max_length=1000,allow_blank=True,allow_null=True)
    # 问题
    question = serializers.IntegerField()
    class Meta:
        model=Question_app
        fields=['id','content','question','section']


# 获取所有问题列表序列化
class QuestionList(serializers.ModelSerializer):
    # 问题所在的课程分类
    course_name = serializers.CharField(source='section.chapter.stage.course.name')



    # 问题所在的阶段
    stage_name = serializers.CharField(source='section.chapter.stage.name')


    # 问题所在的章节
    chapter_name = serializers.CharField(source='section.chapter.name')


    # 问题所在的小节
    section_name=serializers.CharField(source="section.name")





    class Meta:
        model=Question_app
        fields="__all__"


# 获取单个问题序列化

class QuestionRetion(serializers.ModelSerializer):
        # 格式化时间
    create_time=serializers.DateTimeField(format="%Y-%m")

    # 序列化用户名称 那个用户的问题
    user_name=serializers.CharField(source='user.name')
      # 问题所在的课程分类
    course_name = serializers.CharField(source='section.chapter.stage.course.name')



    # 问题所在的阶段
    stage_name = serializers.CharField(source='section.chapter.stage.name')


    # 问题所在的章节
    chapter_name = serializers.CharField(source='section.chapter.name')


    # 问题所在的小节
    section_name=serializers.CharField(source="section.name")
    class Meta:
        model=Question_app
        fields="__all__"

     


     
'''

如果不想在模型中去添加很多的字段 如果需要去用的话，直接在序列化中添加额外的内容
'''

# 选择小节获取所有问题
class SectionSerializers(serializers.ModelSerializer):
    question_app=QuestionList(many=True,read_only=True)
    class Meta:
        model=Section
        fields='__all__'