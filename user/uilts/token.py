'''
jiaoyu_env.user.uilts.token 的 Docstring
Pyjwt身份校验 封装工作类
'''
import jwt
from django.conf import settings
import time
# 生成token
def get_token(data):
    # 设置过期时间
    data.update({'exp':time.time()+settings.JWT_EXPIRATION_DELTA})
    # 生成token ddata 盐  algorithm='HS256'
    token=jwt.encode(data,settings.SECRET_KEY,algorithm='HS256')
    return token

# 校验token
def veriy_token(token):
    try:
        data=jwt.decode(token,settings.SECRET_KEY,algorithms=['HS256'])
    except Exception as f:
        return None
    return data



