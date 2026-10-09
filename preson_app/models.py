from django.db import models

# Create your models here.
# 个人订阅模型
from course_app.models import Course,Section
from user.models import User

class preson_app(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="preson_app",null=True,blank=True,verbose_name="用户名称")
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name="preson_app",null=True,blank=True,verbose_name="课程内容")
    class Meta:
         db_table = 't_user_course'

# 个人收藏模型
class UserSection(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_section",null=True,blank=True,verbose_name="用户名称")
        section=models.ForeignKey(Section,on_delete=models.CASCADE,related_name="user_section",null=True,blank=True,verbose_name="课程小节")
        create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
        class Meta:
            db_table="t_user_section"
