from django.db import models

# Create your models here.

class Poll(models.Model):
    author = models.CharField(max_length=100, blank=False, null=False)
    categories = models.CharField(max_length=20, blank=False, null=False)
    tag = models.CharField(max_length=20, blank=False, null=False)
    post = models.TextField(max_length=1000)
    date_created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.categories