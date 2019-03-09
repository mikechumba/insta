from django.shortcuts import render,redirect
from .models import Profile
from django.contrib.auth.models import User
from .forms import Registration
from django.contrib.auth import login,authenticate

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
         return redirect('photo_home')
   else:
      form = Registration()

   context = {
      'form': form
   }

   return render(request, 'timeline/register.html', context)