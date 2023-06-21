from django.shortcuts import render, redirect
from django.contrib import auth
from .models import User


def signup(request):
    if request.method == 'POST':
        if User.objects.filter(username = request.POST.get("username")).exists():
            return render(request,"Register.html",{"message":"이미 존재하는 회원입니다."})
        else:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
                first_name=request.POST['name'][0],
                last_name=request.POST['name'][1:],
                phone_number=request.POST.get("phonenum"),
                sex=request.POST['sex'],
                age=request.POST['age'],
                grade=request.POST['grade'],
                major=request.POST['major']
            )
            auth.login(request, user)
            return redirect('main:index')

    else:
        return render(request, 'Register.html')

# def profile(request,id):
#     context = {
#         "person" : User.objects.get(id = id)
#     }
#     return render(request, "profile.html",context)
