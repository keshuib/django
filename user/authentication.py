# 校验token
from .uilts.token import veriy_token
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import  User
# user, token
# 校验认证token类 需要继承 BaseAuthentication 
class JWTAuthentication(BaseAuthentication):
    #之后写authenticate方法
    def  authenticate(self,request):
        # 获取前端请求头中的Token
        token=request.headers.get('token')
        if  not token:
            raise AuthenticationFailed("token没有找到")
        else:
            data=veriy_token(token)
            if data:
                try:
                    # 获取登录认证成功后的用户
                    user=User.objects.get(id=data.get('user_id'))
                    return user,token
                except User.DoesNotExist:
                    raise AuthenticationFailed("用户不存在")
            else:
                raise AuthenticationFailed("token已失效")

'''
retrun token user
token 存放在request.anth 已经配置全局验证 会自动验证
但验证成功后 还需要request.user 去获取验证成功的用户


'''
       
     
        
        