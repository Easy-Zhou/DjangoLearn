from django.db import models

# Create your models here.
"""
AutoField  # 自增字段是一个int类型的数据
BigAutoField # 是一个64-bit 的integer 大的自增字段
BigIntegerField # 大整数 -9223372036854775808 to 9223372036854775808 
BinaryField # 二进制类型可以存储文件或者照片
BooleanField  
CharField  字符串类型 有一个必填参数 CharField.max_length  字符的最大长度，Django 会根据这个参数在数据库层和校验层限制该字段允许的最大字符数
TextField  一个容量很大的文本字段  admin管理界面用<textarea>多行编辑表示该字段
DateField # 2019-03-23 auto_now：当对象被保存时,自动将该字段的值设置为当前时间.通常用于表示 “last-modified” 时间戳；
           auto_now_add：当对象首次被创建时,自动将该字段的值设置为当前时间.通常用于表示对象创建时间。
DateTimeField  # 2019-03-23 00:00:00
DecimalField  # 十进制小数  参数 max_digits 小数总长度  decimal_places, 小数位长度
FloatField # 浮点类型
DurationField  storing periods of time, [DD] [HH:[MM:]]SS[.uuuuuu] 表示存储一个时间区间
EmailField  
FileField  存储文件


关系字段(relationship field)

ForeignKey 
ManyToManyField  
OneToOneField 

https://blog.csdn.net/u013210620/article/details/79182870 相关字段的blog
alex的blog：www.cnblogs.com/alex3714/articles/8984718.html
"""


class Account(models.Model):
    """
    账户表
    django 默认有一个自增字段主键如果不写会默认加上，如果自己写了主键则使用自己的
    """
    username = models.CharField(max_length=64, unique=True)  # 唯一字段
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    register_date = models.DateTimeField(auto_now_add=True)  # auto_now_add 表示一创建就会自动加上时间
    signature = models.CharField("签名字段", max_length=255, null=True)  # 引号中的内容用于解释 可以为空

    def __str__(self):
        return self.username


class Article(models.Model):
    """文章表"""

    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    account = models.ForeignKey("Account", on_delete=models.CASCADE)  # 关联删除
    tags = models.ManyToManyField("Tag")  # null 在这里不起作用 stuDatabase.Article.tags: (fields.W340) null has no effect on ManyToManyField.

    pub_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    """标签表"""
    name = models.CharField(max_length=64, unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
