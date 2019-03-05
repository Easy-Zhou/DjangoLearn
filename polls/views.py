from django.shortcuts import render, HttpResponse, redirect


# Create your views here.


def test_get_argument(request):
    id = request.GET['id']  # 获取url中传入的id参数  http://127.0.0.1:8000/polls/get_argument?id=2
    # 或者是 request.GET.get('id')
    return HttpResponse("get id is :%s" % id)


class Person():
    def __init__(self, username):
        self.username = username


def index(request):
    """
    通过context传递的参数可以是python中的所有参数类型
    :param request:
    :return:
    """
    p = Person('这是person类')
    context = {
        'username': 'joy',
        'person': p,
    }
    return render(request, 'index.html', context=context)


def if_tag(request):
    age = request.GET.get('age')
    print(type(age))
    age = int(age)
    context = {
        'age': age
    }

    return render(request, 'if_tag.html', context=context)


def for_in_tag(request):
    context = {
        'books': ['book1', 'book2', 'book3', 'book4'],
        'persons': {
            'username': 'user01',
            'age': 18
        },
        'bookStore': [
            {
                'name': '三国演义',
                'author': '罗贯中',
                'price': 25
            },
            {
                'name': '红楼梦',
                'author': '曹雪芹',
                'price': 25
            }, {
                'name': '西游记',
                'author': '吴承恩',
                'price': 25
            }, {
                'name': '水浒传',
                'author': '施耐庵',
                'price': 25
            }

        ]
    }
    return render(request, 'for_in_tag.html', context=context)


def get_input_test(request):
    return render(request, 'get_input_test.html')


def get_post_value(request):
    username = request.POST['username']
    context = {'username': username}
    #  return render(request, 'get_input_test.html', locals())
    # locals() 可以在前段直接使用变量的名称不用再context中取名,传的变量太多可能会降低效率
    return render(request, 'get_input_test.html', context=context)  # locals() 可以在前段直接使用变量的名称不用再context中取名


def study_redirect(request):
    """
    使用redirect进行重定向
    :param request:
    :return:
    """
    context = {
        'books': {
            'book_name': '三国演义',
            'author': '罗贯中',
            'price': 23
        }

    }

    # return redirect("http://www.baidu.com")
    return redirect("/for_in_tag")
