from django.db import models
from course_app.models import Section
from user.models import User
# Create your models here.
# 提问和回答模型
# 前端用富文文本去做 后端模块接口正常写
class Question_app(models.Model):
    title=models.CharField(null=True,blank=True,max_length=256,verbose_name="问题标题")         
    content=models.TextField(max_length=256,blank=True,null=True,verbose_name="问题内容")
    create_time=models.DateTimeField(blank=True,null=True,verbose_name="创建时间")
    # 提问的用户
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="question_app",blank=True,null=True,verbose_name="提问者")

    # 在那个章节里面提问
    section=models.ForeignKey(Section,on_delete=models.CASCADE,related_name="question_app",null=True,blank=True,verbose_name="章节")



    # 自关联自己 回答问题   
    answers=models.ForeignKey("self",on_delete=models.CASCADE,
                verbose_name='回答',null=True,blank=True,related_name='children')
    class Meta:
        db_table="t_question_app"
