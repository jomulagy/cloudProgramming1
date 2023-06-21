from django.shortcuts import render
from account.models import User
from couple.models import Couple
def index(request):
    man_num = User.objects.filter(sex = "남").count()
    print(man_num)
    woman_num = User.objects.filter(sex = "여").count()
    couple_num = Couple.objects.all().count()
    context = {
        "man_num" : man_num,
        "woman_num" : woman_num,
        "couple_num" :couple_num,
    }
    return render(request,"Home.html",context)
