from django import forms
from .models import *
from django.contrib.auth.forms import SetPasswordForm
# 

class reparationForm(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200)
    description = forms.CharField(widget=forms.Textarea, required=False)


class actuexcel(forms.Form):
    title = forms.CharField(label="excel", max_length=200)
    description = forms.CharField(widget=forms.Textarea, required=False)