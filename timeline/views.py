from django.shortcuts import render,redirect
from .models import Profile,Image
from django.contrib.auth.models import User
from .forms import Registration,ProfileUpdateForm,UserUpdateForm,LoginForm,CommentForm,ImageForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
   user = request.user

   if request.method == 'POST':
      new_post_form = ImageForm()
      if form.is_valid():
         form.save()
         messages.success('Comment added successfully!')
         return redirect('home')
   else:
      new_post_form = ImageForm()

   if request.method == 'POST':
      form = CommentForm()
      if form.is_valid():
         form.save()
         messages.success('Comment added successfully!')
         return redirect('home')
   else:
      form = CommentForm()

   images = Image.objects.all()

   context = {
      'images': images,
      'form': form,
      'user': user,
      'new_post': new_post_form
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


@login_required
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
         user_instance = user_form.save(commit=False)
         profile = form.save(commit=False)
         profile.user = user_instance
         user_instance.save()
         profile.save()
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
         return redirect('home')
   else:
      form = LoginForm()

   context = {
      'form': form
   }

   return render(request, 'registration/login.html', context)

def logout_view(request):
   logout(request)
   return redirect('login')