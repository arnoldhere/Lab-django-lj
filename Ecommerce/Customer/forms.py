from django import forms
from .models import *

class FeedbackForm(forms.ModelForm): 
    # This auto-generates an HTML form using django's ModelForm
    class Meta:
        model = Feedback
        fields = ["email", "message"]


###
# Unlike ModelForm, forms.Form doesn’t know anything about your model — you manually define fields, and you also manually handle saving to DB.

# class FeedbackForm(forms.Form):
#     email = forms.EmailField(label="Your Email", required=True)
#     message = forms.CharField(label="Your Feedback", widget=forms.Textarea, required=True)