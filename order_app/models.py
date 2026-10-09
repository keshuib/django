from django.db import models
from user.models import User
from course_app.models import Course
#学习计划应该在班级中进行
from plan_app.models import ClassType
# Create your models here.

class Order_app(models.Model):
    Order_Type=(
        (0,"未支付"),
        (1,"已支付")
    )

    id=models.CharField(primary_key=True,max_length=255)
    order_type=models.IntegerField(choices=Order_Type,default=0,verbose_name="订单状态")
    # 订单金额 最大10为数字 两位小数
    amount=models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True,verbose_name="订单金额")
    total_amount=models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True,verbose_name="实际订单金额")
    gemt_payment=models.DateTimeField(blank=True,null=True,verbose_name="支付时间")
    # 下单的用户
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="order_app",blank=True,null=True,verbose_name="订单用户")
    # 下单的课程
    coursr=models.ForeignKey(Course,on_delete=models.CASCADE,related_name="order_app",blank=True,null=True,verbose_name="下单的课程")
    # 分配的班级
    classtype=models.ForeignKey(ClassType,on_delete=models.CASCADE,related_name="order_app",blank=True,null=True,verbose_name="分配的班级")
    class Meta:
        db_table="t_order_app"
        