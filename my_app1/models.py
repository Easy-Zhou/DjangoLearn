from django.db import models


# Create your models here.


class Account(models.Model):
    """ 账户表"""

    username = models.CharField(max_length=64, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    register_data = models.DateTimeField(auto_now_add=True)  # 表示当此条记录插入时自动生成当前时间
    signature = models.CharField("签名", max_length=255, null=True)  # 签名表示在使用的时候会进行提示这个字段用来干啥


class Article(models.Model):
    """ 文章表"""

    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    account = models.ForeignKey("Account", on_delete=models.CASCADE)  # 删除了外键 也删除本条文章的记录
    tags = models.ManyToManyField("Tag", null=True)
    pub_date = models.DateTimeField()


class Tag(models.Model):
    """ 标签表"""

    name = models.CharField(max_length=64, unique=True)
    date = models.DateTimeField(auto_now_add=True)
