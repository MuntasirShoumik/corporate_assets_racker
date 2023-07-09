from django import forms
from django.forms import PasswordInput
from .models import Company
from django.core.validators import *
import re

class RegistrationForm(forms.ModelForm):
    class Meta:
        model= Company
        fields = "__all__"



    def pass_check(val):
        if not bool(re.search(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$', val)):
            raise forms.ValidationError("minimum 8 characters in length, At least one uppercase English letter, At least one lowercase English letter, At least one digit, At least one special character!")
         

    name = forms.CharField(max_length=50,label="First name")
    address = forms.CharField(max_length=100,required=True)
    email = forms.EmailField(label="Email",required=True)
    password = forms.CharField(widget=forms.PasswordInput,validators=[pass_check],label="Password",required=True)  



class LoginForm(forms.Form):
    company_name = forms.CharField()
    password = forms.CharField(widget=PasswordInput())