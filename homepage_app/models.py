from django.db import models

# Create your models here.
class RotationChart(models.Model):
    name=models.CharField(max_length=256,verbose_name="轮播名称")
    img=models.CharField(max_length=256,verbose_name="轮播图片")

    class Meta:
        db_table="t_rotation_chart"


# 添加特色服务模型
class  FeatureService(models.Model):
    name=models.CharField(max_length=256,verbose_name="特色服务名称")
    class Meta:
        db_table = 't_feature_service'