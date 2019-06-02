from django.contrib import auth
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from blog.models import UserInfo
from .forms import RegisterForm


def login(request):
    # 如果是ajax请求则进行判断
    if request.is_ajax():
        username = request.POST.get("username")
        password = request.POST.get("password")
        valid_code = request.POST.get("valid_code")
        res = {"state": False, "msg": None}
        s_valid_code = request.session.get("valid_code")
        # 判断验证码是否正确
        if valid_code.upper() == s_valid_code.upper():
            user = auth.authenticate(username=username, password=password)
            if user:  # 若此用户存在则进行登录操作
                res['state'] = True
                auth.login(request, user)
            else:
                res['msg'] = '用户名或者密码错误'
        else:
            res['msg'] = '验证码错误'

        return JsonResponse(res)

    return render(request, 'login.html')


def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    return redirect("/blog/login")  # 若用户未验证则重定向至登录页面


def get_valid_img(request):
    from PIL import Image
    from PIL import ImageDraw, ImageFont
    from random import randint
    import random
    def get_random_color():
        return (randint(0, 255), randint(0, 255), randint(0, 255))

    image = Image.new('RGB', (250, 34), get_random_color())

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("blog/static/font/kumo.ttf", 28)
    temp = []
    for i in range(5):
        random_num = str(randint(0, 9))
        random_low_alpha = chr(randint(97, 122))
        random_upper_alpha = chr(randint(65, 90))
        random_char = random.choice([random_num, random_low_alpha, random_upper_alpha])
        draw.text((24 + i * 36, 0), random_char, get_random_color(), font=font)

        # 保存随机字符
        temp.append(random_char)
    # draw.text((0,0),"python",get_random_color(),font=font)   # 往图片中加文字
    # draw.line()   # 往图片中加线
    # draw.point()  # 往图片中加点

    # with open('valid_code.png', 'wb') as f:
    #     image.save(f, 'png')
    #
    # with open('valid_code.png', 'rb') as f:
    #     data = f.read()
    # 噪点噪线
    width = 250
    height = 34
    for i in range(5):
        x1 = random.randint(0, width)
        x2 = random.randint(0, width)
        y1 = random.randint(0, height)
        y2 = random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill=get_random_color())

    for i in range(20):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=get_random_color())
        x = random.randint(0, width)
        y = random.randint(0, height)
        # 弧线
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=get_random_color())

    # 在内存中生成图片
    from io import BytesIO
    f = BytesIO()
    image.save(f, 'png')
    data = f.getvalue()
    f.close()

    valid_code = "".join(temp)
    request.session["valid_code"] = valid_code

    return HttpResponse(data)


def register(request):
    form = RegisterForm()
    context = {
        'form': form,
    }

    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        res = {'username': None, 'error_dict': None}
        if register_form.is_valid():
            print(register_form.cleaned_data)

            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            avatar = request.FILES.get('avatar')
            if avatar:
                user = UserInfo.objects.create_user(username=username, password=password, email=email, avatar=avatar)
            else:
                user = UserInfo.objects.create_user(username=username, password=password, email=email)
            res['username'] = user.username
        else:
            print(register_form.errors)
            res['error_dict'] = register_form.errors
        return JsonResponse(res)
    return render(request, 'register.html', context=context)  # 也可以使用locals()
