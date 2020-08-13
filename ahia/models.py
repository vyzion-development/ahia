from django.db import models
from PIL import Image
from django.utils import timezone
from django.urls import reverse
import os
from django.conf import settings
# Create your models here.
# model branch
#User model we refer to these as "Students" for now


class Profile(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  name = models.CharField(max_length=50, null=False, blank=False )
  age = models.DateField(null=False, blank=False)
  bio = models.TextField(max_length=350, null=False, blank=False)
  location = models.CharField(max_length=85, null=False, blank=False)
  image = models.ImageField(default='default.jpg', upload_to='profile_pics')

  def __str__(self):
    return self.name

#Category Model for the categories of assets if needed
class Category(models.Model):

  name = models.CharField(max_length = 200)

  def __str__(self):
       return self.name

  def save(self, *args, **kwargs):
         super(settings.AUTH_USER_MODEL, self).save(*args, **kwargs)


         img = Image.open(self.image.path)

         if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

#Asset model 
class Asset(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assets')
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
            return self.asset_title


#Model for Posting in timeline so people can see your post
class Post(models.Model):
 	post_title = models.CharField(max_length=100)
 	post_asset = models.ForeignKey(Asset, null=True,blank=True, on_delete=models.CASCADE, related_name="posts")
 	Post_content = models.TextField()
 	post_date_posted = models.DateTimeField(default=timezone.now)
 	post_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")

 	def __str__(self):
 		return self.title

 	def extension(self):
 		name, extension = os.path.splitext(self.file.name)
 		return extension


 	def get_absolute_url(self):
 		return reverse('post-detail', kwargs={'pk': self.pk})



#Chat model for messaging if needed 
class Chat(models.Model):
  chat_sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="sender", on_delete=models.CASCADE)
  chat_receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="receiver", on_delete=models.CASCADE)
  chat_msg = models.TextField(max_length=1000)
  chat_timestamp = models.DateTimeField(auto_now_add=True)

  def __str__(self):
   return str(self.id) + ": from " + str(self.sender) + " to " + str(self.receiver)
      
# #Comment model for commenting on post 
class Comment(models.Model):
  com_body = models.TextField()
  com_pub_time = models.DateTimeField()

  com_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  com_ebook = models.ForeignKey(Asset, on_delete=models.CASCADE)



  def pub_date_pretty(self):
   return self.pub_time.strftime('%b %e %Y')

