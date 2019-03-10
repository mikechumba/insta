from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class Registration(UserCreationForm):
   '''
   Form that extends the UserCreationForm

   Added fields are the name and email fields.
   '''
   username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
   email= forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), max_length=64)
   password1= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
   password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))


   class Meta(UserCreationForm.Meta):
      model = User
      fields = UserCreationForm.Meta.fields + ("email","username","password1")
   

