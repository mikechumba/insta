from django.shortcuts import render,redirect
from .models import Profile,Image,Comments,Followed,Follows,Like
from django.contrib.auth.models import User
from .forms import Registration,ProfileUpdateForm,UserUpdateForm,LoginForm,CommentForm,ImageForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import _EnsureCsrfCookie 

# Create your views here.
@login_required(login_url='register')
def index(request):
   user = request.user
   comments = Comments.objects.all()

   if request.method == 'POST':
      form = CommentForm(request.POST)
      if form.is_valid():
         image_id = request.POST["image_id"]
         comment = form.save(commit=False)
         comment.comment_author = user.profile
         comment.commented_on_id = int(image_id)
         comment.save()
         return redirect('home')
   else:
      form = CommentForm()

   images = Image.objects.order_by('-time_posted')

   context = {
      'images': images,
      'form': form,
      'user': user,
      'comments': comments
   }
   return render(request, 'timeline/timeline.html', context)

@login_required
def users(request,user_name):
   user = User.objects.filter(username=user_name).first()
   images = Image.objects.filter(author=user.profile)

   context = {
      'user': user,
      'images': images
   }

   return render(request, 'timeline/user.html', context)

@login_required
def new_post(request):
   user = request.user
   if request.method == 'POST':
      form = ImageForm(request.POST,request.FILES)
      if form.is_valid():
         image = form.save(commit=False)
         image.author = user.profile
         image.save()
         return redirect('home')
   else:
      form = ImageForm()


   context = {
      'form': form
   }

   return render(request, 'timeline/new-post.html', context)

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

   user = request.user
   images = Image.objects.filter(author=user.profile)

   context = {
      'user': user,
      'images': images
   }

   return render(request, 'timeline/profile.html', context)

@login_required
def edit_profile(request):

   user = request.user

   if request.method == 'POST':
      form = ProfileUpdateForm(request.POST,request.FILES,instance=user.profile)
      user_form = UserUpdateForm(request.POST,instance=user)
      if user_form.is_valid() and form.is_valid():
         user_form.save()
         profile = form.save(commit=False)
         profile.user = user
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

@login_required
def search(request):

   if 'insta_search' in request.GET and request.GET["insta_search"]:
      searched = request.GET.get("insta_search")
      if searched:
         user = User.objects.filter(username=searched).first()

   context = {
      'searched': searched,
      'user': user
   }

   return render(request, 'timeline/search.html', context)


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


@login_required
def logout_view(request):
   logout(request)
   return redirect('login')


@login_required
def image_view(request,image_id):

   user = request.user

   image = Image.objects.filter(pk=image_id).first()
   comments = Comments.objects.filter(commented_on=image)

   if request.method == 'POST':
      form = CommentForm(request.POST)
      if form.is_valid():
         image_id = request.POST["image_id"]
         comment = form.save(commit=False)
         comment.comment_author = user.profile
         comment.commented_on_id = int(image_id)
         comment.save()
         return redirect('home')
   else:
      form = CommentForm()

   context = {
      'image': image,
      'comments': comments,
      'form': form
   }

   return render(request,'timeline/image_view.html',context)


def like(request,image_id):

   user = request.user

   image = Image.objects.filter(pk=image_id).first()
   like = image.like_set.filter(liked_by=user.profile).first()
   # like = Like.objects.get(liked=image,liked_by=user.profile)

   if like:
      like.delete()
   else:
      Like.likes(image,user.profile)

   return redirect('home')

def follow(request,user_name):

   user = request.user
   follows = Follows.objects.filter(profile=user.profile)
   followed_user = User.objects.filter(username=user_name).first()
   if user.profile not in follows:
      Follows.follow(user.profile)
      Followed.follow()
      return redirect('profile')
   else:
      Follows.objects.get(following=user.profile).delete()
      return redirect('profile')