from django.shortcuts import render, redirect

# Create your views here.
from .models import SessionUserInfo


def index(request):
    username = request.session.get("username")
    if not username:
        return redirect('/l_session/login')
    return render(request, 'l_index.html', {'username': username})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        user_o = SessionUserInfo.objects.filter(name=user, pwd=pwd).first()
        if user_o:
            request.session["username"] = user_o.name
            request.session['user_id'] = user_o.pk
            return redirect("/l_session/index")

        else:
            return render(request, 'login.html')


def logout(request):

    request.session.flush()
    return redirect('/l_session/index')
