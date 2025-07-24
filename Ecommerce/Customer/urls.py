from django.urls import path
from .views import *

urlpatterns = [
    # Common routes
    path("test/", Test, name="test"),
    path("", Home, name="home"),
    path("demo/", Demo, name="demo"),
    path("about/", About, name="about"),
    path("contact/", Contact, name="contact"),
    # Auth Routes
    path("signup/", Signup, name="signup"),
    path("login/", loginview, name="login"),
    # User Access Routes
    
]
