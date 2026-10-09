from django.db import models
# 使用werkzeyg加密密码
from werkzeug.security import check_password_hash,generate_password_hash
# Create your models here.
# 使用djngo自带的hasher 去加密 更符合django生态
from django.contrib.auth.hashers import check_password,make_password

'''
在模型中去给密码进行加密处理

'''
import os
from uuid import uuid4
# 生成文件名称 避免重名文件
def get_imge(imagename:str):
    ext=os.path.splitext(imagename)[-1]
    name=uuid4().hex()
    return f'img/{name}{ext}'
# 创建用户模型 可用于登录注册功能
'''
注册时 用户 密码 手机号是必要的
登录时 手机号 和密码
其他的都是在登录之后显示的用户页面 不包括密码


'''
class User(models.Model):
    name=models.CharField(max_length=256,null=False,blank=False,unique=True,verbose_name='用户名称')
    phone=models.CharField( max_length=11,null=False,unique=True,blank=True,verbose_name='手机号')
    pwd=models.CharField(max_length=256,null=False,blank=False,verbose_name="密码")
    SEIZ_CHOICE=(('male','男'),
('female','女'))
    size=models.CharField(max_length=256,blank=True,null=True,choices=SEIZ_CHOICE,verbose_name='性别')
    age=models.IntegerField(blank=True,null=True,verbose_name="年龄")
    job_title=models.CharField(max_length=256,null=True,verbose_name='职位')
    introduction=models.CharField(max_length=256,blank=True,null=True,verbose_name="简介")
    avatar=models.ImageField(upload_to=get_imge,null=True,blank=True)

    create_at=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    update_at=models.DateTimeField(auto_now=True,verbose_name="更新时间")
# 表名
    class Meta:
        db_table='t_user'
        verbose_name='用户模型'

# # 加密密码 存储到数据库 pip install werkzeug
#     @property 
#     def password(self):
#         return self.pwd
#     # 调用 self.pwd 放回给属性 password   self.pwd=>password 
#     @password.setter
#     def password(self,pwd):
#         # 将加密的密码直接赋值给 self.pwd 也就是password
#         self.pwd=generate_password_hash(pwd)
#     # 数据库保存 password=>self.pwd
#     # 验证passwoed (self.pwd)
#     def chek_password(self,pwd):
#         return check_password_hash(self.pwd,pwd)
    
    # django加密密码 
    def set_password(self,raw_password:str):
        # 直接调用self.pwd 并将加密后的内容赋值给他  raw_password是用户输入的密码
        self.pwd=make_password(raw_password)

    # 校验密码
    def check_password(self,raw_password:str):
        return check_password(raw_password,self.pwd)


    # 转成json数据to_dict()

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "size": self.size,
            "age": self.age,
            "job_title": self.job_title,
            "introduction": self.introduction,
            "avatar": self.avatar.url if self.avatar else None,
            "create_at": self.create_at.strftime("%Y-%m-%d %H:%M:%S"),
            "update_at": self.update_at.strftime("%Y-%m-%d %H:%M:%S")
        }



    












    
   



    

    
