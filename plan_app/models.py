from django.db import models

# Create your models here.
from course_app.models import Course
# 学习计划
class Plan(models.Model):
    name = models.CharField(max_length=20,verbose_name='计划名称')
    introduction = models.TextField(blank=True,null=True,verbose_name='计划介绍')
    info = models.TextField(blank=True,null=True,verbose_name='计划信息')

    course = models.ForeignKey(Course,related_name='plan',on_delete=models.CASCADE,verbose_name='课程',null=True,blank=True)

    class Meta:
        db_table = 't_plan'
    

'''
学习计划应该在班级中进行
'''
# 建立班级模块
class ClassType(models.Model):
  name = models.CharField(max_length=20,verbose_name='班级名称')
  price = models.DecimalField(max_digits=8,decimal_places=2,verbose_name='价格')
  all_stage = models.IntegerField(blank=True,null=True,verbose_name='所有阶段',default=1)
  supervision = models.IntegerField(blank=True,null=True,verbose_name='督导',default=1)
  update = models.IntegerField(blank=True,null=True,verbose_name='update service',default=1)
  homework = models.IntegerField(blank=True,null=True,verbose_name='作业',default=1)
  online = models.IntegerField(blank=True,null=True,verbose_name='线上',default=1)
  work = models.IntegerField(blank=True,null=True,verbose_name='work in join',default=1)
  remote = models.IntegerField(blank=True,null=True,verbose_name='远程',default=1)

  course = models.ForeignKey(Course,related_name='class_type',on_delete=models.CASCADE,verbose_name='课程',null=True,blank=True)
  class Meta:
    db_table = 't_class_type'
    
