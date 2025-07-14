from django.urls import path
from .views import *

urlpatterns = [
    path("test/", Test, name="test"),
    path("demo/", Demo, name="demo"),
    path("about/", About, name="about"),
    path("contact/", Contact, name="contact"),
]
