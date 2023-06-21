from django.shortcuts import render, redirect
from account.models import User
from couple.models import Couple

def matching1(request):

    return render(request,"matched2.html")

def matching2(request,grade):
    context = {
        "grade" : grade
    }
    return render(request,"matched3.html",context)

def matching3(request,grade,age):
    context = {
        "grade": grade,
        "age": age,
    }
    return render(request,"matched4.html",context)

def matching4(request,grade,age,major):
    context = {
        "grade": grade,
        "age": age,
        "major": major,
    }
    return render(request,"matched5.html",context)

def matchList(request,grade,age,major,address):
    if request.user.sex == "남":
        sex = "여"
    else:
        sex = "남"

    if request.GET.get("age") == "연하":
        matched = User.objects.filter(sex = sex,grade = grade,age__gt = age,address = address,major = major).exclude(id = request.user.id)
    elif request.GET.get("age") == "연상":
        matched = User.objects.filter(sex = sex,grade = grade,age__lt = age,address = address,major = major).exclude(id = request.user.id)
    else:
        matched = User.objects.filter(sex = sex,grade = grade,age = age,address = address,major = major).exclude(id = request.user.id)

    context = {
        "matched":matched
    }
    return render(request,"matched6.html",context)

def coupleCreate(request):
    if request.method == "POST":
        user1 = User.objects.get(username = request.POST.get("user1"))
        user2 = User.objects.get(username = request.POST.get("user2"))
        if user1.sex == "남":
            new = Couple(man = user1,woman = user2)
            new.save()
        else:
            new = Couple(man = user2,woman = user1)
            new.save()
        return redirect("main:index")

    else:
        return render(request,"coupleEnroll.html")
