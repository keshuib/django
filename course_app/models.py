from django.db import models

# Create your models here.
#生成文件名称的重复问题
# import os
# from uuid import uuid4
# def imge(imgename:str):
#     ext=os.path.splitext(imgename)[-1]
#     name=uuid4().hex
#     return f'img/{name}{ext}'







# 创建课程分类模块
class Course(models.Model):
    name=models.CharField(max_length=256,verbose_name="课程分类名称")
    learn_info=models.CharField(max_length=256,null=True,blank=True,verbose_name="课程学习信息")
    learn_style=models.CharField(max_length=256,null=True,blank=True,verbose_name="课程学习方法")
    learn_time=models.CharField(max_length=256,null=True,blank=True,verbose_name="课程学习时间")
    # icon=models.ImageField(upload_to=imge,verbose_name="课程分类图标")
    supervision = models.CharField(blank=True,null=True,max_length=255,verbose_name='课程监督方式')
    icon=models.CharField(max_length=256,null=True,blank=True,verbose_name="课程分类图标")
    brief=models.CharField(max_length=256,null=True,blank=True,verbose_name="课程分类简介")
    level=models.IntegerField(blank=True,null=True,verbose_name="课程分类级别")
    
    class Meta:
        db_table="t_course"











# 课程阶段模块 
'''
选中某一个分类用很多个阶段 课程分类与课程阶段是关联的 

'''
class Stage(models.Model):
    name=models.CharField(max_length=256,verbose_name="课程阶段名称")
    introduction=models.CharField(max_length=256,null=True,blank=True,verbose_name="课程阶段介绍")
    level=models.IntegerField(blank=True,null=True,verbose_name="课程阶段级别")
    is_free=models.IntegerField(null=True,blank=True,verbose_name="是否免费")
    # 课程阶段分类
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='stage',null=True,blank=True,verbose_name="课程分类")
    class Meta:
        db_table='t_stage'
















# 课程章节
'''
每一个课程阶段都有对应的课程章节
'''
class Chapter(models.Model):
    name=models.CharField(max_length=256,verbose_name="课程章节的名称")
    level=models.IntegerField(null=True,blank=True,verbose_name="课程章节的级别")
    # 每个阶段对应的章节
    stage=models.ForeignKey(Stage,on_delete=models.CASCADE,related_name='chapter',null=True,blank=True,verbose_name="课程阶段")
   
    class Meta:
        db_table='t_chapter'



# 课程小结
'''

每个章节下面要有对应的小结

'''
class Section(models.Model):
    name=models.CharField(max_length=256,verbose_name="课程小结名称")
    is_must = models.IntegerField(blank=True,null=True,verbose_name='是否必修')
    duration = models.IntegerField(blank=True,null=True,verbose_name='课程时长')
    learned_count = models.IntegerField(blank=True,null=True,verbose_name='学习人数')
    url = models.CharField(blank=True,null=True,max_length=255,verbose_name='课程小节视频地址')
    chapter=models.ForeignKey(Chapter,on_delete=models.CASCADE,related_name='sction',blank=True,null=True,verbose_name="课程章节")
    
    class Meta:
        db_table="t_section"






