from django.shortcuts import render, HttpResponse


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
