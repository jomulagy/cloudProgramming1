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

                phone_number=request.POST.get("phone_num"),
                sex=request.POST['sex'],
                age=request.POST['age'],
                address = requs.POST['address'],
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
