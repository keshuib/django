from django.urls import path
from .views import *
urlpatterns = [
    path('login/',Userviewp.as_view()),
    # 旧接口保留：前端历史代码使用了拼写错误的 regiser 路径。
    path("regiser/",ResgisterView.as_view()),
    path("register/",ResgisterView.as_view()),
    path("user/<int:id>/",UserView.as_view())
   
]
