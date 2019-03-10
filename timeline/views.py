from django.shortcuts import render,redirect
from .models import Profile
from django.contrib.auth.models import User
from .forms import Registration,ProfileUpdateForm,UserUpdateForm,LoginForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
# Create your views here.
def index(request):

   profiles = User.objects.all()

   context = {
      'profiles': profiles
   }
   return render(request, 'timeline/timeline.html', context)


def register(request):

   if request.method == 'POST':
      form = Registration(request.POST)
      if form.is_valid():
         form.save()
         username = form.cleaned_data.get('username')
         raw_password = form.cleaned_data.get('password1')
         user = authenticate(username=username, password=raw_password)
         login(request, user)
         user = User.objects.filter
         return redirect('edit_profile')
   else:
      form = Registration()

   context = {
      'form': form
   }

   return render(request, 'timeline/register.html', context)

def profile(request):

   user = User.objects.filter(username = 'mikechumba').first()

   context = {
      'user': user
   }

   return render(request, 'timeline/profile.html', context)


def edit_profile(request):

   user = User.objects.filter(username = 'mikechumba').first()

   if request.method == 'POST':
      form = ProfileUpdateForm(request.POST, instance=request.user)
      user_form = UserUpdateForm(request.POST, request.FILES, instance=request.user.profile)
      if user_form.is_valid() and form.is_valid():
         user_form.save()
         form.save()
         messages.info(request, 'You\'ve successfully updated your account!')
         return redirect('profile')
   else:
      form = ProfileUpdateForm(instance=request.user)
      user_form = UserUpdateForm(instance=request.user.profile)

   context = {
      'user': user,
      'user_form': user_form,
      'form': form
   }

   return render(request, 'timeline/edit-profile.html', context)


def login_view(request):
   if request.method == 'POST':
      form = LoginForm()
      if form.is_valid():
         username = form.cleaned_data.get('username')
         raw_password = form.cleaned_data.get('password1')
         user = authenticate(username=username, password=raw_password)
         login(request, user)
         redirect('home')
   else:
      form = LoginForm()

   context = {
      'form': form
   }

   return render(request, 'timeline/login.html', context)