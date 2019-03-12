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
   author = models.ForeignKey(Profile, on_delete=models.CASCADE)
   time_posted = models.DateField(auto_now=True)
   
   def __str__(self):
      return self.caption

class Like(models.Model):

   liked = models.ForeignKey(Image, on_delete=models.CASCADE)
   liked_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

   @classmethod
   def likes(cls,img,prfl):
      like = cls(liked=img,liked_by=prfl)
      return like.save()

   def delete_like(self):
      like = Like.objects.all(self)
      return like.delete()

class Comments(models.Model):
   
   comment = models.CharField(max_length=140)
   comment_author = models.ForeignKey(Profile, on_delete=models.CASCADE)
   commented_on = models.ForeignKey(Image, on_delete=models.CASCADE)

   def __str__(self):
      return self.comment

class Followed(models.Model):

   followers = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followed_by',null=True)

   def __str__(self):
      return self.followers

   @classmethod
   def follow(cls,prfl):
      follow = cls(followers=prfl)
      return follow.save()

class Follows(models.Model):

   following = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following',null=True)

   def __str__(self):
      return self.following

   @classmethod
   def follow(cls,prfl):
      follow = cls(following=prfl)
      return follow.save()