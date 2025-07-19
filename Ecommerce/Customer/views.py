import email
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# Create your views here.
def Test(req):
    return HttpResponse("Hello there...")


def Demo(req):
    return render(req, "demo.html", {"name": "Arnold..."})


def About(req):
    feedbacks = Feedback.objects.all().order_by(
        "-createdAt"
    )  # Fetch all feedback records latest first
    return render(req, "about.html", {"feedbacks": feedbacks})


def Home(req):
    return render(req, "Home.html")


def loginview(req):
    if req.method == "POST":
        email = req.POST.get("email")
        password = req.POST.get("password")
        print(email, password)
        user = authenticate(req, username=email, password=password)
        print(user)
        if user is not None:
            login(req, user)
            print("User logged in successfully...")
            messages.success(req, f"Welcome back, {user.first_name}!")
            return redirect("home")
        else:
            messages.error(req, "Invalid username or password.")
    return render(req, "login.html")


def Signup(req):
    if req.method == "POST":
        form = SignupForm(req.POST)
        if form.is_valid():
            form.save()
            print("User created successfully...")
            messages.success(req, "Registered succesfully....!")
            return redirect("login")
        else:
            messages.error(req, "Please correct the errors below.")
    else:
        form = SignupForm()
    return render(req, "signup.html", {"form": form})


def Contact(req):
    if req.method == "POST":
        form = FeedbackForm(req.POST)
        if form.is_valid():
            form.save()  # insert record in db
            print("Feeback submited...")
            messages.success(req, "Thank you for your feedback!")
            return redirect("contact")  # or reload same page with success msg
    else:
        form = FeedbackForm()
    return render(req, "contact.html", {"form": form})


""" Signup view to handle user registration for custom User model"""
"""
def Signup(req):
    if req.method == "POST":
        first_name = req.POST.get("first_name")
        last_name = req.POST.get("last_name")
        email = req.POST.get("email")
        password = req.POST.get("password")
        # phone = req.POST.get('phone')

        # check is user already exists !!
        if User.objects.filter(email=email).exists():
            messages.error(req, "Email is already in use......")
        else:
            user = User.objects.create_user(
                username=email,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
            )
            user.save()
            messages.success(req, "User created successfully!")
            return redirect("login")
    else:
        return render(req, "signup.html")
"""


##
"""
def Contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Extract data from cleaned form
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Manually create and save model instance
            feedback = Feedback(email=email, message=message)
            feedback.save()

            return redirect('feedback')  # or show a success message
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form})
"""
## Total manually form handling without even using model forms
"""Comparison of Form Handling Methods
| Method               | Code Style            | DB Save                     | Validation       |
| -------------------- | --------------------- | --------------------------- | ---------------- |
| `ModelForm`          | Djangoic (high-level) | `form.save()`               | Built-in (Model) |
| `forms.Form`         | Mid-level control     | `Model.objects.create(...)` | Customizable     |
| Manual POST handling | Full manual           | `Model.objects.create(...)` | Fully manual     |
"""
