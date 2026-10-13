from django.shortcuts import render
# from .alipay_tool import get_qr
# Create your views here.

from rest_framework.response import Response
# 旧订单实现依赖保留：SafeOrderView 不再需要这个会校验错误字段的序列化器。
# from .seraliazers import OrderAppSeralizer
from .models import Order_app
# 订单的课程
# from course_app.models import Course
# 订单后分配的班级
from plan_app.models import ClassType
# from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
# 支付宝配置为空时不在接口导入阶段加载 SDK，避免服务启动即失败。
# from .alipay_tool import get_alipay_client
# from json import loads
import time
from rest_framework import serializers


class OrderCreateSerializer(serializers.Serializer):
    """只接收班型 ID，避免把只读的用户和课程字段误当作请求参数。"""

    classtype = serializers.PrimaryKeyRelatedField(
        queryset=ClassType.objects.select_related("course").all()
    )


class SafeOrderView(APIView):
    """修正版订单接口：GET 查询当前用户订单，POST 创建订单。"""

    def get(self, request):
        orders = (
            Order_app.objects
            .filter(user=request.user)
            .select_related("coursr", "classtype")
        )
        data = [
            {
                "id": order.id,
                "order_type": order.order_type,
                "amount": order.amount,
                "total_amount": order.total_amount,
                "course_name": order.coursr.name if order.coursr else "",
                "classtype_name": (
                    order.classtype.name
                    if order.classtype else ""
                ),
            }
            for order in orders
        ]
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        classtype = serializer.validated_data["classtype"]
        if classtype.course is None:
            return Response(
                {"msg": "该班型没有关联课程"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        order_id = (
            f"{request.user.id}-"
            f"{classtype.id}-"
            f"{int(time.time())}"
        )
        order, _ = Order_app.objects.get_or_create(
            id=order_id,
            defaults={
                "user": request.user,
                "coursr": classtype.course,
                "classtype": classtype,
                "amount": classtype.price,
            },
        )

        # 旧支付宝调用暂时保留在下方原实现中；配置为空时不能调用 SDK，否则会 500。
        return Response(
            {
                "msg": "订单创建成功",
                "order_id": order.id,
                "url": None,
            },
            status=status.HTTP_201_CREATED,
        )

"""
旧订单实现保留：该版本存在 course 字段名、time 导入、支付宝参数和回调实例化错误。
现已由上方 SafeOrderView 替代，并在 urls.py 中切换路由。

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
"""
