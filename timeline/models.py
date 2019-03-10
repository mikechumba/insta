from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):

   user = models.OneToOneField(User, on_delete=models.CASCADE)
   avatar = models.ImageField(upload_to='avatar/', default='default.jpg')
   bio = models.TextField(max_length=140, blank=True, default='')

   def __str__(self):
      return f'{self.user.username}'
   
class Image(models.Model):

   img = models.ImageField(upload_to='', height_field=None, width_field=None, max_length=None)
   caption = models.TextField(max_length=280)
   img_name = models.CharField(max_length=50)
   author = models.ForeignKey(Profile, on_delete=models.CASCADE)
   time_posted = models.DateField(auto_now=True)
   likes = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name='liked_by', null=True)
   
   def __str__(self):
      return self.caption

class Comments(models.Model):
   
   comment = models.CharField(max_length=140)
   comment_author = models.ForeignKey(Profile, on_delete=models.CASCADE)
   

   def __str__(self):
      return self.comment

class Follow(models.Model):

   followers = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followed_by')
   following = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')

   def __str__(self):
      return self.followers