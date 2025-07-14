from django.urls import path
from .views import *
urlpatterns = [
    path("demo/", Demo, name="Demo"),
    path("test/", Test, name="Test"),
    path("home/", Home, name="home"),
    path("about/", About, name="about"),
]