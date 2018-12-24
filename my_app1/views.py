from django.shortcuts import render, HttpResponse  # HttpResponse 是将返回给浏览器的一些数据封装到一些此方法中


# Create your views here.


def test_view(request):
    print("执行业务逻辑", request)
    print(dir(request))

    return HttpResponse("执行了第一次django请求")


def login_view(request):
    """

    :param request:
    :return:
    """

    # method 不填默认为get（向后台获取数据） 则会将表单中的数据显示在地址栏中，
    # method 为 post（向后台提交数据）则不会显示在地址栏中
    # 但是因为django 的机制是不能随意向后台提交数据因此会出现错误，需要其他方法解决
    html = """
            <form method="post">
            <input type="text" name="username" />
            <input type="password" name="password" />
            <input type="submit" value="登陆">
        </form>
    """
    print("login view")

    return HttpResponse(html)


def index_view(request):
    """

    :param request:
    :return:
    """

    # print("index view")

    return render(request, 'lab6-2.html')


def article_2018(request):
    return HttpResponse("article_2018")


def article_archive(request, year):
    return HttpResponse("this is %s" % year)


def article_archive2(request, arg1, arg2):
    return HttpResponse("year is %s month is %s" % (arg1, arg2))


def article_archive3(request, year, month, slug):
    return HttpResponse("year is %s month is %s slug is %s" % (year, month, slug))


def convert_test(request, year):
    return HttpResponse("使用自定义的转换器来接瘦year参数 year=%s" % year)


def path1(request):
    return HttpResponse("extra 聚合path1")


def path2(request):
    return HttpResponse("extra 聚合path2")

