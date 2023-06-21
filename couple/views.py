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

    if age == "연하":
        print(1)
        matched = User.objects.filter(sex = sex,grade = grade,age__lt = request.user.age,address = address,major = major)
        print(User.objects.filter(sex = sex,grade = grade,age__lt = request.user.age))
    elif age == "연상":
        print(2)
        matched = User.objects.filter(sex = sex,grade = grade,age__gt = request.user.age,address = address,major = major)
    else:
        print(4)
        matched = User.objects.filter(sex = sex,grade = grade,age = request.user.age,address = address,major = major)

    print(matched.count())
    if matched.count()>0:
        print(1)
        context = {
            "matched":matched[0]
        }
    else:
        context = {
            "matched" :None,
        }
    print(context)
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
