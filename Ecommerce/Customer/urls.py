from django.urls import path
from .views import *

urlpatterns = [
    path("test/", Test, name="test"),
    path("", Home, name="home"),
    path("demo/", Demo, name="demo"),
    path("about/", About, name="about"),
    path("contact/", Contact, name="contact"),
    path("signup/", Signup, name="signup"),
    path("login/", loginview, name="login"),
]
