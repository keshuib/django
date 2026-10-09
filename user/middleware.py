# # 自定义中间件去验证token
# from .uilts.token import veriy_token
# from django.http import JsonResponse
# from rest_framework import status
# from .models import User

# class LoginMiddleware:
#     # 初始化数据
#     def __init__(self,get_response):
#         self.get_response=get_response

#     # 方法
#     def __call__(self, request):
#             #登录和注册功能不需要验证
#              public_paths = {
#             "/api/user/login/",
#             "/api/user/register/", }
#              if request.path not in public_paths:
#                   token = request.META.get("HTTP_AUTHORIZATION")
#                   if not token:
#                         return JsonResponse({"msg":"请先登录"},status=status.HTTP_400_BAD_REQUEST)
#                   else:
#                          data = veriy_token(token)
#                          if not data:
#                                return JsonResponse({"msg":"登录失效"},status=status.HTTP_400_BAD_REQUEST)
#                          else:
#                                 try:
#                                         # 获取登录认证成功后的用户
#                                         request.current_user = User.objects.get(pk=data["user_id"])
#                                 except User.DoesNotExist:
#                                       return JsonResponse(
#                     {"msg": "用户不存在"},
#                     status=status.HTTP_401_UNAUTHORIZED,
#                 )       
#              else:
#                    return self.get_response(request)
                   

            
           