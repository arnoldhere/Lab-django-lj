from dataclasses import field
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FeedbackForm(forms.ModelForm):
    # This auto-generates an HTML form using django's ModelForm
    class Meta:
        model = Feedback
        fields = ["email", "message"]


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1"]
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['email']  # using email as username
        if commit:
            user.save()
        return user


###
# Unlike ModelForm, forms.Form doesn’t know anything about your model — you manually define fields, and you also manually handle saving to DB.

# class FeedbackForm(forms.Form):
#     email = forms.EmailField(label="Your Email", required=True)
#     message = forms.CharField(label="Your Feedback", widget=forms.Textarea, required=True)
