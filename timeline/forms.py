from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Profile,Comments

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
   

class ProfileUpdateForm(forms.ModelForm):
   '''
   Profile update form. 

   Allows user to add a bio and a custom avatar.
   '''

   class Meta:
      model = Profile
      fields = ['avatar','bio']
      widgets = {
         'bio': forms.Textarea(attrs={'placeholder': 'Bio'})         
      }

class UserUpdateForm(forms.ModelForm):
   '''
   User update form.

   A user can add their name
   '''
   first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
   last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
   class Meta:
      model = User
      fields = ['first_name','last_name']

class LoginForm(AuthenticationForm):
   '''
   Login form.

   Takes a username and password
   '''
   username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
   password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
   class Meta:
      model = User
      fields = ['username', 'password']


class CommentForm(forms.ModelForm):
   '''
   Comment form
   '''
   class Meta:
      model = Comments
      fields = ['comment']
      widgets = {
         'comment': forms.TextInput(attrs={'placeholder': 'Add a Comment'})        
      }