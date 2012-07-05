from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=60)
    body=models.TextField()
    created=models.DateField()
    updated=models.DateField()
    def __unicode__(self):
        return ''

class Comment(models.Model):
    
    body=models.TextField()
    author=models.CharField(max_length=60)
    created=models.DateField()
    updated=models.DateField()
    post=models.ForeignKey(Post)
    def __unicode__(self):
        return ''

