from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from user.models import User
from course_app.models import Section
from user.uilts.token import veriy_token
from .serializers import QuestionSeralizer, AnswerAddSerializer,QuestionList,QuestionRetion,SectionSerializers
from .models import Question_app
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

# 问题模块 提交问题
class QuestionAppViews(APIView):
    def post(self,request,format=None):
        # 获取前端数据 request.data
        # 反序列化
        ser= QuestionSeralizer(data=request.data)
        # 判断序列化是否成功
        if ser.is_valid():
                # 获取提交的问题来自那个小节
                section=Section.objects.filter(pk=ser.validated_data['section']).first()
                if not section:
                    return Response({"msg":"小节不存在"}, status=status.HTTP_404_NOT_FOUND)
                    # 添加数据
                Question_app.objects.create(user=request.user,section=section, title=ser.validated_data['title'],
        content=ser.validated_data['content'],)
                return Response({"msg":"提交成功","status":status.HTTP_200_OK})
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
           


# 回答提交的问题的内容

class AnswerView(APIView):
      def post(self,request,format=None):
        # 获取前端数据 request.data
        # 反序列化
        ser= AnswerAddSerializer(data=request.data)
        # 判断序列化是否成功
        if ser.is_valid():
                    # 获取提交的问题来自那个小节
                    section=Section.objects.filter(pk=ser.validated_data['section']).first()
                    # 获取问题
                    question=Question_app.objects.filter(pk=ser.validated_data['question']).first()
                    if not section or not question:
                        return Response({"msg":"小节或问题不存在"}, status=status.HTTP_404_NOT_FOUND)
                    # 添加回答
                    Question_app.objects.create(user=request.user,section=section,answers=question,
        content=ser.validated_data['content'],)
                    return Response({"msg":"回答成功"},status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

'''
对用户是全都需要看见的
对后端只要没有回答的问题就行
'''
# 获取问题列表 还没有回答的问题  没有已经回答过的
class QuestionViews(generics.ListAPIView):
    # 问题列表允许浏览，但提交问题仍由全局 JWT 认证保护。
    authentication_classes = []

    queryset=Question_app.objects.filter(answers=None).order_by("-create_time")
    serializer_class=QuestionList



# 获取单个问题 路由加参数 pk  
class QuestionView(generics.RetrieveAPIView):
    # 问题详情允许浏览，但修改类接口仍由全局 JWT 认证保护。
    authentication_classes = []

    queryset=Question_app.objects.all()
    serializer_class=QuestionRetion

# 选中小节 获取所有问题 只要没有回答的问题
class SectionQuestionView(generics.ListAPIView):
    # 小节问题列表允许公开浏览。
    authentication_classes = []

    # 旧实现保留：查询 Question_app 却使用 SectionSerializers，序列化对象类型不匹配。
    # queryset=Question_app.objects.filter(answers=None).order_by("-create_time")
    queryset=Section.objects.all()
    serializer_class=SectionSerializers











