from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path('', views.index, name="home"),
   path('register', views.register, name='register'),
   path('profile', views.profile, name='profile'),
   path('profile/edit', views.edit_profile, name='edit_profile'),
   path('login/', views.login_view, name='login'),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]