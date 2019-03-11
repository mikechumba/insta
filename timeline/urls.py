from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

urlpatterns = [
   path('', views.index, name="home"),
   path('register', views.register, name='register'),
   path('profile', views.profile, name='profile'),
   path('timeline/new', views.new_post, name='new_post'),
   path('profile/edit', views.edit_profile, name='edit_profile'),
   path('<user_name>', views.edit_profile, name='user_profile'),
   path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm), name='login'),
   path('logout/', views.logout_view, name='logout'),
]