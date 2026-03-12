from django.urls import path
from .views import ask_ai,index

urlpatterns = [
    path("",index, name="index"),
    path("ask/", ask_ai, name="ask_ai"),

]
