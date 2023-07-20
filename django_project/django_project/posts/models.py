from django.db import models 

# Create your models here.
class Post(models.Model): # new
    text = models.TextField()
from django.db import models 

class Post(models.Model):
     text = models.TextField()

     def __str__(self):
        return self.text[:50]