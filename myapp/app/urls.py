from django.urls import path
from . import views,home,welcome

urlpatterns = [
    path("", welcome.index,name="index"),
    path("upload/",views.index,name="view"),
    path("lab/",home.Home,name="home"),
]
