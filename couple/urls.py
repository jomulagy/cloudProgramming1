from django.urls import path
from .views import *

app_name = "couple"

urlpatterns = [
    path("match/list/",matchList, name= "mathchList"),
    path("couple/create/",coupleCreate, name= "couplecreate"),

]
