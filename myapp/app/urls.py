from django.urls import path
from . import views,home,welcome

urlpatterns = [
    path("", welcome.index,name="index"),
    path("upload/",views.index,name="view"),
    path("nur/",home.Home,name="home"),
    path("post/",views.index,name="index"),
    path("nur/",home.Home,name="home")
]
