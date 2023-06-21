from django.urls import path
from .views import *

app_name = "couple"

urlpatterns = [
    path("matching1/",matching1, name= "matching1"),
    path("matching2/<str:grade>/",matching2, name= "matching2"),
    path("matching3/<int:grade>/<str:age>/",matching3, name= "matching3"),
    path("matching4/<int:grade>/<str:age>/<str:major>/",matching4, name= "matching4"),

    path("match/list/<int:grade>/<str:age>/<str:major>/<str:address>/",matchList, name= "mathchList"),
    path("couple/create/",coupleCreate, name= "couplecreate"),

]
