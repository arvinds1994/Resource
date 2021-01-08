from django import forms
from .models import Resource

class LoginForm(forms.Form):

    username = forms.CharField(max_length=10)
    password = forms.CharField(min_length=5)

class ResourceForm(forms.ModelForm):

    class Meta:
        model = Resource
        exclude = ['added_on']
