from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from django.conf.urls import url

from . import views

urlpatterns = [
   path('', views.index, name="photo_home"),
   path('register', views.register, name='register'),
   path('profile', views.profile, name='profile'),
   path('profile/edit', views.edit_profile, name='edit_profile')
]