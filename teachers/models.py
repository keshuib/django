from django.db import models

# Create your models here.
class Teacher(models.Model):
    name=models.CharField(max_length=256,verbose_name="教师姓名")
    brief=models.CharField(max_length=256,null=True,blank=True,verbose_name="教师简介")
    avatr=models.CharField(max_length=256,null=True,blank=True,verbose_name="教师头像")
    position=models.CharField(max_length=256,null=True,blank=True,verbose_name="教师职位")
    characteristic = models.CharField(null=True,blank=True,max_length=256,verbose_name='教师特点')



    class Meta:
        db_table="t_teacher"


    def to_dict(self):
        return {
            "name":self.name,
            "brief":self.brief,
            "avatr":self.avatr,
            "ppstion":self.position,
            "characteristic":self.characteristic


        }