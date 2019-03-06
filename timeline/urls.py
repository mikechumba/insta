from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from django.conf.urls import url

from . import views

urlpatterns = [
   path('', views.index, name="photo_home"),
]