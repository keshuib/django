from django.urls import path
from .views import SafeOrderView

urlpatterns=[
    # 旧路由保留：CreateOrderViews 使用了错误的 course/time/支付宝参数。
    # path("orders/", CreateOrderViews.as_view())
    path("orders/", SafeOrderView.as_view())
]
