from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    #POST 요청이 들어오면 로그인 처리를 해줌
    if request.method == 'POST':

        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('blog')
        else:
            return render(request, 'login.html')

    #GET 요청이 들어오면 ligin form을 담고 있는 login.html을 띄어줌
    else:
        return render(request, 'login.html')