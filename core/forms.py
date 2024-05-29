from django import forms
from .models import *

class PasswordResetForm(forms.Form):
    email = forms.EmailField(label="Correo electrónico", max_length=254)