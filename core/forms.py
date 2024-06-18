from django import forms
from .models import *
from django.contrib.auth.forms import SetPasswordForm
from crud.models import region
# 

class reparationForm(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200)
    description = forms.CharField(widget=forms.Textarea, required=False)


class actuexcel(forms.Form):
    title = forms.CharField(label="excel", max_length=200)
    description = forms.CharField(widget=forms.Textarea, required=False)
   
class RegionForm(forms.Form):
   region = forms.ModelChoiceField(queryset=region.objects.all(), label="Selecciona una región") 