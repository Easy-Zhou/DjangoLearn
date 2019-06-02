from django.shortcuts import render
from . import models


# Create your views here.

def operate_database(request):
    # 直接创建
    models.Account.objects.create(
        username="jack",
        email="jack@126.com",
        password='jack123'
    )

    # 或者使用字典的形式
    models.Account.objects.create(**{'username': "sss", 'email': 'see@qq.com', 'password': 'jasfsd'})

    # 分步创建数据

    new_user_obj = models.Account(
        username='test',
        email='test@126.com',
        password='123',
        signature='this is a test account'
    )

    new_user_obj.save()  # save 了之后才会存入数据库中

    # 亦或者
    account = models.Account()
    account.username = 'tt'
    account.email = 'ere@126.com'
    account.password = '1234'
    account.save()
    ##

    models.Tag.objects.create(
        name='科普'
    )

    models.Tag.objects.create(
        name='小说'
    )

    models.Tag.objects.create(
        name='新闻'
    )

    models.Tag.objects.create(
        name='自传'
    )

    article = models.Article()
    article.title = "这是个测试"
    article.content = "这是内容"
    article.account_id = 9  # 通过Account 表中的id来选择关联的外键
    # article.account = account # 通过上面的account对象来进行外键关联
    article.save()

    # 多对多的关联需要在对象创建完成之后才能进行设置
    article.tags.set([9, 10])

    article.tags.set([9, ])  # 这样就重新变成了1 相当于重新赋值

    article.tags.add(11, 10)  # 这个是在原有的基础上加上某些值

    return render(request, 'index.html')


def query_database(request):
    """
    数据库查询
    :param request:
    :return:
    """
    ##############查询操作################
    # 返回了所有的数据 以QuerySet的形式返回对象
    models.Account.objects.all()

    # 获取一个id=2 的数据（只能查一条，但是其效率更高），是一个User对象，查询不到会报错，不建议使用
    models.Account.objects.get(id=10)

    # and 的形式 还有其他的方式 id__gt=1 great than id__gte great than equal id__lt
    models.Account.objects.filter(id=1, password='jack123')

    # 一下为一些过滤条件
    models.Account.objects.filter(password__startswith='jack')  # 过滤条件

    models.Account.objects.filter(email__contains="@126.com")  # 包含 默认大小写敏感
    models.Account.objects.filter(email__icontains="@126.com")  # 大小写不敏感
    models.Account.objects.filter(id__in=[1, 2])

    # range 区间过度，可以对数字、日期进行过滤
    import datetime
    start_date = datetime.datetime(2019, 3, 6)
    end_data = datetime.datetime(2019, 3, 7)
    models.Account.objects.filter(register_date__range=(start_date, end_data))
    # 其他日期查询
    models.Article.objects.filter(pub_data__date='2019-03-05')
    models.Account.objects.filter(register_date__gt='2019-03-06')

    # 连表查询
    models.Article.objects.filter(account__username='jack')  # 返回的是一个queryset

    # many2many
    models.Article.objects.filter(account__username='jack')[0]
    models.Article.objects.filter(account__username='jack')[0].tags.all()

    # isnull
    models.Article.objects.filter(pub_data__isnull=True)

    # 正则表达式
    models.Account.objects.filter(username__regex=r'^([sj])')  # iregex 大小写不敏感

    # 外键反向关联操作
    a = models.Account.objects.get(username='alex')
    a.article_set.all()  # 反向 article_set
    a.article_set.select_related()  # 与all的关联一样

    # 多对多操作
    o = models.Article.objects.all()[1]
    o.tags.all()
    # <QuerySet [<Tag: 投资>, <Tag: 科技>]>

    # 多对多反向操作
    t = models.Tag.objects.get(name="投资")
    t.article_set.all()

    return render(request, 'index.html')


def querySet_stu(request):
    """
    QuerySet 的一些操作
    :param request:
    :return:
    """
    a = models.Account.objects.all()
    a.values()
    """
    output:
     <QuerySet [{'id': 9, 'username': 'jack', 'email': 'jack@126.com', 'password': 'jack123', 'register_date': datetime.datetime(2019, 3, 5, 18, 29, 38, 336125, tzinfo=<UTC>), 'signature': None},
      {'id': 10, 'username': 'sss', 'email': 'see@qq.com', 'password': 'jasfsd', 'register_date': datetime.datetime(2019, 3, 5, 18, 29, 38, 338357, tzinfo=<UTC>), 'signature': None},
       {'id': 11, 'username': 'test', 'email': 'test@126.com', 'password': '123', 'register_date': datetime.datetime(2019, 3, 5, 18, 29, 38, 339550, tzinfo=<UTC>), 'signature': 'this is a test account'}, 
       {'id': 12, 'username': 'tt', 'email': 'ere@126.com', 'password': '1234', 'register_date': datetime.datetime(2019, 3, 5, 18, 29, 38, 340748, tzinfo=<UTC>), 'signature': None}]>
    """
    a.values('username')
    """output:
    < QuerySet[{'username': 'jack'}, {'username': 'sss'}, {'username': 'test'}, {'username': 'tt'}] >
    """
    a.values('username', 'password')

    # 排序
    a.values('id', 'register_date').order_by('id')  # 升序
    a.values('id', 'register_date').order_by('-id')  # 降序
    a.values('id', 'register_date').order_by('id', 'register_date')  # 多字段排序
    a.values('id', 'register_date').order_by('id').reverse()  # 反转

    # 如需取后5条，但此处切片不能负着切 但是可以反转之后再取 但是reverse() 需要再order_by之后再进行reverse

    # exclude 排除
    models.Account.objects.exclude(register_date__date='2019-03-06')

    return render(request, 'index.html')


def updateOrdelete(request):
    """
    数据库的改删操作
    :param request:
    :return:
    """

    # 批量修改 返回影响的行数
    models.Account.objects.filter(username='jack').update(password="jack#21")

    # 单条修改
    obj = models.Account.objects.get(username='linux')
    obj.username = 'python'
    obj.save()

    # 批量删除
    models.Account.objects.filter(password='jack123').delete()

    # 单条删除
    obj = models.Account.objects.get(id=3)
    obj.delete()

    return render(request, 'index.html')
