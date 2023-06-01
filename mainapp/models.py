from django.db import models

# Create your models here.

class News(models.Model):
    author = models.CharField( max_length=50)
    title = models.CharField( max_length=255)
    dis = models.TextField()
    content = models.TextField()
    image_url = models.CharField( max_length=255)
