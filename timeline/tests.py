from django.test import TestCase
from .models import Image,Profile,Like,Comments
from django.contrib.auth.models import User
# Create your tests here.

# Functions to create instances from models
def create_user_instance():
   user = User(username='mikechumba',email='mike@test.com',password='password')
   return user

def create_profile_instance():
   profile = Profile(avatar='default.jpg',bio='Someone someone')
   return profile

def create_image_instance(profile_instance):
   image = Image(img='avatar.jpg',caption='some kind of avatar',author_id=profile_instance)
   return image

def create_comments_instance(profile_instance,image_instance):
   comment = Comments(comment='Wow!',comment_author=profile_instance,commented_on=image_instance)
   return comment

def create_like_instance(profile_instance,image_instance):
   liked = Like(liked=image_instance,liked_by=profile_instance)
   return liked


class UserProfileTest(TestCase):

   def setUp(self):
      self.new_user = create_user_instance()
      
   def test_user_instance(self):
      self.assertTrue(isinstance(self.new_user,User))

   def test_save_user(self):
      self.new_user.save()
      users = User.objects.all()
      self.assertTrue(len(users),1)

class ProfileTest(TestCase):

   def setUp(self):
      self.user = create_user_instance()
      self.user.save()

   def test_profile_created_for_every_user(self):
      profiles = Profile.objects.all()
      users = User.objects.all()
      self.assertEqual(len(profiles),len(users))

   def test_profile_data(self):
      avatar = self.user.profile.avatar
      self.assertEqual(avatar,'default.jpg')

class ImageTest(TestCase):

   def setUp(self):
      user = create_user_instance()
      user.save()
      self.new_image = create_image_instance(user.profile.id)

   def test_image_instance(self):
      self.assertTrue(isinstance(self.new_image,Image))

   def test_save_image(self):
      self.new_image.save_image()
      images = Image.objects.all()
      self.assertTrue(len(images),1)

   def test_update_caption(self):
      self.new_image.update_caption('I changed it')
      self.assertEqual(self.new_image.caption,'I changed it')

   def test_delete_image(self):
      self.new_image.save_image()
      self.new_image.delete_image()
      images = Image.objects.all()
      self.assertTrue(len(images)<1)

class LikesTest(TestCase):

   def setUp(self):
      user = create_user_instance()
      user.save()
      image = create_image_instance(user.profile.id)
      image.save()
      self.new_like = create_like_instance(user.profile,image)

   def test_like_instance(self):
      self.assertTrue(isinstance(self.new_like,Like))

   def test_save_likes(self):
      self.new_like.save()
      likes = Like.objects.all()
      self.assertTrue(len(likes),1)

   def test_delete_likes(self):
      self.new_like.save()
      self.new_like.delete_like()
      likes = Like.objects.all()
      self.assertTrue(len(likes)<1)



