from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

class EnquiryForm(forms.ModelForm):
	class Meta:
		model=models.Enquiry
		fields=('full_name','email','detail')

class SignUp(UserCreationForm):
	class Meta:
		model=User
		fields=('first_name','last_name','email','username','password1','password2')