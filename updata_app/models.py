from django.db import models

# Create your models here.

from course_app.models import Course,Stage

class UpdateCourse(models.Model):
  TYPE_CHOICES = (
     (0,'升级'),
     (1,'新增')
   )
  name = models.CharField(max_length=100,verbose_name='更新的课程标题')
  introduction = models.TextField(blank=True,null=True,verbose_name='介绍')
  info = models.TextField(blank=True,null=True,verbose_name='课程信息')
  create_time = models.DateTimeField(blank=True,null=True,auto_now_add=True,verbose_name='创建时间')
  update_type = models.IntegerField(null=True,blank=True,choices=TYPE_CHOICES,verbose_name='更新类型')

  course = models.ForeignKey(Course,blank=True,null=True,on_delete=models.SET_NULL,verbose_name='课程分类')
  stage = models.ForeignKey(Stage,blank=True,null=True,on_delete=models.SET_NULL,verbose_name='阶段')

  class Meta:
    db_table = 't_update_course'
