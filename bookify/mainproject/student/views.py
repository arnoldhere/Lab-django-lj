from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def Demo(request):
    return HttpResponse("Hello, this is a demo view for the student app.")

def Test(request):
    return render(request, "test.html")

def Home(req):
    return render(req, "home.html")

def About(req):
    return render(req, "about.html")