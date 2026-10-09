from django.db import models

# Create your models here.
from teachers.models import Teacher
from course_app.models import Stage
class FreeCourse(models.Model):
   price=models.IntegerField(blank=True,null=True,verbose_name="课程价格")
   img=models.CharField(max_length=256,blank=True,null=True,verbose_name="课程图片")
   start_time=models.DateTimeField(blank=True,verbose_name="开始时间")
   end_time=models.DateTimeField(blank=True,verbose_name="结束时间")
   #限免课程应该在课程阶段里 每个阶段有多个限免课程
   stage=models.ForeignKey(Stage,on_delete=models.CASCADE,related_name="freecourse",null=True,blank=True,verbose_name="课程阶段")
      # 每个讲师有多个限免课程
   teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name="freecourse",null=True,blank=True,verbose_name="课程讲师")

   class Meta:
      db_table="t_freecourese"


 
