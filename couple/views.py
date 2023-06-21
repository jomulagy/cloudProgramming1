from django.shortcuts import render, redirect
from account.models import User
from couple.models import Couple

def matchList(request):
    if request.user.sex == "남":
        sex = "여"
    else:
        sex = "남"
    matched = User.objects.filter(sex = sex,grade = request.POST.get('grade'),age = request.POST.get('age'),address = request.POST.get('address'),major = request.POST.get('major')).exclude(id = request.user.id)
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
