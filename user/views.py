from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from rest_framework import status
from user.uilts.token import get_token
from  rest_framework.response import Response
# Create your views here.


# 用户登录功能
'''

前端获取的信息 在数据库中才能登录
同时验证密码
jwt身份鉴权 生成token 校验token 抽象成认证组件自动执行。
'''
class Userviewp(APIView):
    # 设置登录限流
    throttle_scope = 'login'
    # 登录不校验Token 
    authentication_classes=[]

    def post(self,reuqest):
        # 获取前端传来的数据 
        phone=reuqest.data.get('phone')
        pwd=reuqest.data.get("pwd")
        try:
            user=User.objects.get(phone=phone)
            # 验证密码
            if user.chek_password(pwd):
                # 给id签发token 
                token=get_token({'user_id':user.id})
                # 将token以字典的形式返回前端
                return Response({"status":status.HTTP_200_OK,"msg":"验证成功","data":{"token":token}})
            else:
                return Response({"status":status.HTTP_400_BAD_REQUEST,"msg":"验证失败"})
        except User.DoesNotExist:
            return Response({"status":status.HTTP_404_NOT_FOUND,"msg":"找不到对应用户"})


from .serializers import Userserializer
# 注册功能
'''
注册功能时 有手机号注册 因此需要判断手机号是否注册了



'''
class ResgisterView(APIView):
    # 注册功能不携带token  
    authentication_classes=[]
    # 添加用户
    def post(self,reuqest):
        # 获取前端用户信息 request.data 直接获取全部数据
        # 反序列化 将json数据转化成字典
        ser=Userserializer(data=reuqest.data)
        #验证数据
        if ser.is_valid():
            # 添加数据
            ser.save()
            # 返回可视化页面
            return Response({"status":status.HTTP_200_OK,"msg":"注册成功"})
        else:
             return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "msg": "注册失败",
            "errors": ser.errors})
        


# 获取注册用户的信息(获取个人信息 以及 删除 更新)
from rest_framework import generics
class UserView(generics.RetrieveUpdateAPIView):
    # 获取查询集 直接查询所有 id在urls中加
    queryset=User.objects.all()
    # 指定序列器
    serializer_class=Userserializer
    


       



