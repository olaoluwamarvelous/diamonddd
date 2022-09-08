from django.db import models
from django.db.models import Q
# Create your models here.
class teamdetail(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    point = models.CharField(max_length=100)
    twitter = models.URLField()
    fbook = models.URLField()
    insta = models.URLField()
    linkden = models.URLField()
    photo = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class testimonyp(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=100)
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name + '' + self.message[:30]

class ContactModel(models.Model):
    name = models.CharField(max_length=10055)
    subject= models.CharField(max_length=3066)
    cv = models.FileField(upload_to='file/')
    email=models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    messagess = models.TextField()
    class Meta:
        ordering = ['-created']

    def __str__(self):
       return self.name + '' + self.messagess + '' + self.subject


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    photo = models.ImageField(upload_to='image/')
    image = models.ImageField(upload_to='imagerr/')
    author = models.CharField(max_length=9887)
    mblockquote = models.TextField()
    intro = models.CharField(max_length=9887)
    Body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    email=models.EmailField()
    body= models.TextField(max_length=30)

    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name  +   '    '    +   self.email




