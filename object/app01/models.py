from django.db import models

# Create your models here.
from django.db import models
# Create your models here.
class login(models.Model):
    id=models.AutoField(primary_key=True)#创建一个自增的主键字段
    id_card=models.CharField(null=False,max_length=10)#创建一个varchar类型的字段
    name=models.CharField(null=False,max_length=30)#创建一个varchar类型的字段
    password=models.CharField(null=False,max_length=30)#创建一个varchar类型的字段
    sex=models.CharField(null=False,max_length=5)#创建一个varchar类型的字段

class content(models.Model):
    id = models.AutoField(primary_key=True)  # 创建一个自增的主键字段

    content = models.CharField(null=False, max_length=2000)  # 创建一个varchar类型的字段
# for x in login.objects.all():
#     print(x.name)
print(content.objects.all())