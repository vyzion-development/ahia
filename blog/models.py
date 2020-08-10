from django.db import models
from ahia .models import Asset 
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import os

class Post(models.Model):
 	post_title = models.CharField(max_length=100)
 	post_asset = models.ForeignKey(Asset, null=True,blank=True, on_delete=models.CASCADE)
 	Post_content = models.TextField()
 	post_date_posted = models.DateTimeField(default=timezone.now)
 	post_author = models.ForeignKey(User, on_delete=models.CASCADE)

 	def __str__(self):
 		return self.title

 	def extension(self):
 		name, extension = os.path.splitext(self.file.name)
 		return extension

 	def get_absolute_url(self):
 		return reverse('post-detail', kwargs={'pk': self.pk})




