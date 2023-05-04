from django import forms
from django.forms import ModelForm
from .models import *



class Registrationform(forms.Form):
    class Meta:
        model = RegistrationPage
        fields = "__all__"
        