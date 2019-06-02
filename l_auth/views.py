from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    username = request.user.username  # 若未登录成功则user对象未Anonymous
    # if not username:
    if not request.user.is_authenticated:
        return redirect('/auth/login')
    return render(request, 'l_index.html', {'username': username})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        user_o = auth.authenticate(username=user, password=pwd)
        if user_o:
            # request.session["username"] = user_o.name
            # request.session['user_id'] = user_o.pk
            auth.login(request, user_o)
            # login 函数的操作：request.session['user_id']=user_o.pk request.user=user_o(向session注入user对象)
            return redirect("/auth/index")

        else:
            return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/auth/index')

def register(request):
    username = 'zhou'
    password = 'root123'
    email = '12345@163.com'
    User.objects.create_user(username=username,password=password,email=email)  # 创建普通用户
    User.objects.create_superuser(username=username,password=password,email=email)  # 创建超级用户
