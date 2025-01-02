from django.db import models

class Post(models.Model):
    session_id = models.CharField(max_length=100)
    content = models.TextField()

# Create your models here.
