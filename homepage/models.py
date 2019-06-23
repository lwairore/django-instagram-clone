from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Image(models.Model):
    # image = models.CharField(max_)
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/', default='/home/karangu/Desktop/Instagram\ clone/media')
    uploaded_by = models.ForeignKey(User, default=1)
    # profile_pic = models.For
    comments = models.CharField(max_length =1000, default="Not comments yet")

    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

class Follow(models.Model):
    user_id = models.IntegerField()
    # following_id = models.ForeignKey(User, default=0)
    following_id = models.IntegerField(default=0)

   
# from django.db import models

# class Fruit(models.Model):
#     name = models.CharField(max_length=100, primary_key=True)

class Comments(models.Model):
    comment = models.TextField()
    