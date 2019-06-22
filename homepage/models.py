from django.db import models

# Create your models here.
class Image(models.Model):
    # image = models.CharField(max_)
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/', default='/home/karangu/Desktop/Instagram\ clone/media')
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()