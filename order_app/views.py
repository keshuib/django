from django.shortcuts import render
# from .alipay_tool import get_qr
# Create your views here.

from rest_framework.response import Response
from .seraliazers import OrderAppSeralizer
from .models import Order_app
# 订单的课程
from course_app.models import Course
# 订单后分配的班级
from plan_app.models import ClassType
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from .alipay_tool import get_alipay_client
from json import loads

# 创建添加订单接口
class CreateOrderViews(APIView):
    def post(self,request):
        # 获取前端订单信息 request.data
        # 序列化
        ser=OrderAppSeralizer(data=request.data)
        # 判断是否合法
        if ser.is_valid():
            # 获取登录用户信息 request.user
            # 获取对应的班级
            classtype=ClassType.objects.filter(pk=ser.validated_data['classtype']).first()
            # 获取课班级和用户id
            order_id=f'{request.user.id}{classtype.id}(int(time()))'
            # 创建对应的模型
            Order_app.objects.get_or_create(id=order_id,user=request.user,course=classtype.Course,classtype=classtype,amount=classtype.price)
            # 获取支付二维码
            info=f'{classtype.course.name}-{classtype.name}-{classtype.price}'
            content = get_alipay_client(order_id,info,float(classtype.price))
             # 将content数据转换为字典
            content = loads(content)
            qr_code = content.get('qr_code')
            # 返回数据
            return Response({"msg":"创建成功",'url':qr_code},status=status.HTTP_200_OK)
        else:
            return Response(ser.errors)
        
# 支付成功回调接口
class PayCallBack(APIView):
    def post(self,request):
        # 获取订单单号
        out_trade_no=request.POST.get("out_trade_no")
        # 获取支付时间
        get_payment=request.POT.get("get_payment")
        # 获取订单支付金额
        total_amount=request.POST.get("total_amount")
        # 获取订单信息
        order=Order_app.objects.get(id=out_trade_no)
        # 修改订单状态
        Order_app.order_type=1
        Order_app.total_amount=total_amount
        Order_app.gemt_payment=get_payment
        # 保存支付信息
        Order_app.save()
        return Response({"msg":"支付成功"},status=status.HTTP_200_OK)
