# 序列化
from rest_framework import serializers
from .models import User


class Userserializer(serializers.ModelSerializer):
    # 判断用户手机号是否被注册 必须为validate_phone 否则不会被DRF自动作为校验方法
    def validate_phone(self,value):
        try:
            User.objects.get(phone=value)
            raise serializers.ValidationError("手机号已经被注册")
        except User.DoesNotExist:
            return value

    class Meta:
        # 指定序列化模型
        model=User
        # 指定要序列化的字段
        # fields='__all__'
        # 不序列
        exclude =('create_at','update_at')


    # DRF序列器会默认存储的是明文密码 需要重写create()方法
    # 重写create()方法 调用之前写过的加密算法 避免在保存时 明文保存
    # def create(self,validated_data):
    #     # 把明文密码取出来
    #     pwd=validated_data.pop('pwd')
    #     # 对应用户
    #     user=User(**validated_data)
    #     # 将用户中的密码进行加密存储
    #     user.password=pwd
    #     user.save()
    #     return user


    # django加密重写create()
    def create(self,vaildate_data):
        raw_password=vaildate_data.pop("pwd")
        user=User(**vaildate_data)
        user.set_password(raw_password)
        user.asave()
        return user





        
    

