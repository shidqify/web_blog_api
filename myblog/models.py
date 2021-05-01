from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    summary = models.TextField(max_length=200)
    body = models.TextField(max_length=5000)
    dateposted = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)
    dateupdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title