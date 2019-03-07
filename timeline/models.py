from django.db import models

# Create your models here.
class Profile(models.Model):

   name = models.CharField(max_length=50)
   username = models.CharField(max_length=50)
   email = models.EmailField(max_length=254)
   avatar = models.ImageField(upload_to='avatar/', height_field=None, width_field=None, max_length=None)
   bio = models.TextField(max_length=140)

   def __str__(self):
      return self.name
   
