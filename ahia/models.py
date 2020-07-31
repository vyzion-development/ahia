from django.db import models
from PIL import Image
from django.utils import timezone
from django.urls import reverse
import os
# Create your models here.
# model branch
#User model we refer to these as "Students" for now
class User(models.Model):
  name = models.CharField(max_length=50, null=False, blank=False )
  user_name = models.CharField(max_length=80, null=False, blank=False)
  user_age = models.DateField(null=False, blank=False)
  user_bio = models.TextField(max_length=350, null=False, blank=False)
  location = models.CharField(max_length=85, null=False, blank=False)
  user_avi = models.ImageField(default='default.jpg', upload_to='profile_pics')

  def __str__(self):
    return self.title

#Category Model for the categories of assets if needed
# class Category(models.Model):

#   name = models.CharField(max_length = 200)

#   def __str__(self):
#         return self.name

#   def save(self, *args, **kwargs):
#         super(User, self).save(*args, **kwargs)

#         img = Image.open(self.image.path)

#         if img.height > 300 or img.width > 300:
#             output_size = (300, 300)
#             img.thumbnail(output_size)
#             img.save(self.image.path)

#Asset model 
class Asset(models.Model):
  asset_type = models.CharField(max_length=10, null=False, blank=False)
  asset_title = models.CharField(max_length=100, null=False, blank= False)
  asset_description = models.TextField(max_length=350, null=False, blank=False)
  asset_update = models.DateField(null=False, blank=True)
  #need to add upload too directory to upload the user file and this may not be the right directory
  asset_upload = models.FileField(upload_to = 'downloads//%Y/%m/%d', null=False, blank=True)
  #this is the want which acts as thr price in case of transaction
  asset_want = models.CharField(max_length=200, null=False, blank=False)
  #this is for the category of the files if we add them
  

  def __str__(self):
        return self.title

#Model for Posting in timeline so people can see your post
<<<<<<< HEAD
# class Post(models.Model):
# 	post_title = models.CharField(max_length=100)
# 	post_asset = models.ForeignKey(Asset, null=True,blank=True,upload_to='Files')
# 	Post_content = models.TextField()
# 	post_date_posted = models.DateTimeField(default=timezone.now)
# 	post_author = models.ForeignKey(User, on_delete=models.CASCADE)
=======
class Post(models.Model):
	post_title = models.CharField(max_length=100)
	post_asset = models.ForeignKey(Asset, null=True,blank=True, on_delete=models.CASCADE)
	Post_content = models.TextField()
	post_date_posted = models.DateTimeField(default=timezone.now)
	post_author = models.ForeignKey(User, on_delete=models.CASCADE)
>>>>>>> master

# 	def __str__(self):
# 		return self.title

# 	def extension(self):
# 		name, extension = os.path.splitext(self.file.name)
# 		return extension

# 	def get_absolute_url(self):
# 		return reverse('post-detail', kwargs={'pk': self.pk})



<<<<<<< HEAD
# #Chat model for messaging if needed 
# class Chat(models.Models):
#   chat_sender = models.ForeignKey(User, related_name="sender")
#   chat_receiver = models.ForeignKey(User, related_name="receiver")
#   chat_msg = models.TextField(max_length=1000)
#   chat_timestamp = models.DateTimeField(auto_now_add=True)
=======
#Chat model for messaging if needed 
class Chat(models.Model):
  chat_sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
  chat_receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE)
  chat_msg = models.TextField(max_length=1000)
  chat_timestamp = models.DateTimeField(auto_now_add=True)
>>>>>>> master

#   def __str__(self):
#       return str(self.id) + ": from " + str(self.sender) + " to " + str(self.receiver)
      
<<<<<<< HEAD
# #Comment model for commenting on post 
# class Comment(models.Model):
#     com_body = models.TextField()
#     com_pub_time = models.DateTimeField()
#     com_user = models.ForeignKey(User, on_delete=models.CASCADE)
#     com_ebook = models.ForeignKey(Asset, on_delete=models.CASCADE)
=======
#Comment model for commenting on post 
class Comment(models.Model):
    com_body = models.TextField()
    com_pub_time = models.DateTimeField()
    com_user = models.ForeignKey(User, on_delete=models.CASCADE)
    com_ebook = models.ForeignKey(Asset, on_delete=models.CASCADE)
>>>>>>> master


#     def pub_date_pretty(self):
#         return self.pub_time.strftime('%b %e %Y')

