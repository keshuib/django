from django.shortcuts import render
from .serializers import PresonSerializer,UserSectionSerializer,OrderSerializers
from order_app.models import Order_app
from django.http import JsonResponse
from user.uilts.token import veriy_token
from rest_framework.views import APIView
from rest_framework import status
from .models import preson_app,UserSection
from user.models import User
from course_app.models import Section
from rest_framework.response import Response
# Create your views here.


# 通过token作为唯一标识 去获取（所有）用户数据 用手机号去判断用户是否存在



'''
token全局验证 会自动认证token  

除了登录注册业务其他的都需要去认证token  request.user获取验证成功的用户

如果使用中间件 只需要将登录认证成功后的用户改成request.current_user

'''
class PresonViews(APIView):
    def get(self,request,format=None):
            # 获取对应用户的个人订阅课程
            '''
            - filter(user=request.user)：筛选当前登录用户的订阅；
- select_related("course")：同时联表取出每条订阅关联的课程，后续读取 course.name 不再额外查数据库。
如果接口只返回订阅表自身字段，根本不访问 course.name(额外添加的字段) 那就不需要
            '''
            user_course=preson_app.objects.filter(user=request.user).select_related('course')
            # 序列化
            ser=PresonSerializer(user_course,many=True)
            # 返回前端
            return Response(ser.data,status=status.HTTP_200_OK)

# 获取个人收藏
class UserSectionViews(APIView):
    def get(self,request,format=None):
                    # 额外获取了session  select_related('section')可写可不写 但建议写上
                    user_section=UserSection.objects.filter(user=request.user).select_related('section')
                    # 序列化
                    ser=UserSectionSerializer(user_section,many=True)
                    # 返回前端
                    return Response(ser.data,status=status.HTTP_200_OK)
    # 增加收藏信息
    '''
    在添加之前仍需要去判断用户是否登录  用户是否存在 以及该用户的收藏信息是否有
    '''  
    def post(self,request,format=None):
        #  reuqest.data是前端的信息
        # 序列化
        ser=UserSectionSerializer(data=request.data)
        # 判断是否序列化成功
        if ser.is_valid():
                section=Section.objects.filter(pk=ser.validated_data['section']).first()
                # 添加信息
                if not section:
                    return Response({"msg":"小节不存在"},status=status.HTTP_404_NOT_FOUND)
                else:
                    created=UserSection.objects.get_or_create(user=request.user,section=section)
                    # 返回数据
                return Response({"msg":"收藏成功" if created else  "已收藏"},status={
                status.HTTP_201_CREATED
                if created
                else status.HTTP_200_OK
                })
        

# 获取订单列表
class Orderviews(APIView):
       def get(self,request):
            #   获取订单列表 
            order_app=Order_app.objects.filter(user=request.user).select_related('courser','classtype')
            # 序列化
            ser=OrderSerializers(order_app,many=True)
            # 返回数据
            return Response(ser.data,status=status.HTTP_200_OK)
       

       




                