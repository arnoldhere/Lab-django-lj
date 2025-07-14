from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import *
from django.contrib import messages


# Create your views here.
def Test(req):
    return HttpResponse("Hello there...")


def Demo(req):
    return render(req, "demo.html", {"name": "Arnold..."})


def About(req):
    return render(req, "about.html")


# def Contact(req):
#     return render(req, "contact.html")


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
"""
def feedback_raw_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Optional: manually check if values are not empty
        if email and message:
            Feedback.objects.create(email=email, message=message)
            return redirect('feedback')  # or render with success message
        else:
            return render(request, 'feedback.html', {'error': 'All fields are required!'})

    return render(request, 'feedback.html') 
"""
"""Comparison of Form Handling Methods
| Method               | Code Style            | DB Save                     | Validation       |
| -------------------- | --------------------- | --------------------------- | ---------------- |
| `ModelForm`          | Djangoic (high-level) | `form.save()`               | Built-in (Model) |
| `forms.Form`         | Mid-level control     | `Model.objects.create(...)` | Customizable     |
| Manual POST handling | Full manual           | `Model.objects.create(...)` | Fully manual     |
"""