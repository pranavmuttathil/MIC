from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path('login/',views.register,name="login"),
    path('register/', views.login, name="register")
]