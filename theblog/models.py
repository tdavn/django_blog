from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# from tinymce import models as tinymce_models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))  # id is the same as pk
        return reverse('home') 

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile/')
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    tweeter_url = models.CharField(max_length=255, null=True, blank=True)
    github_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return str(self.user)

class Post(models.Model):
    title = models.CharField(max_length=255, default='title here')
    # ImageGield is set to accept a null (not every post has an image), and set the upload folder.
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    title_tag = models.CharField(max_length=255, default="Freakin' Blog!") # optionally leave out default value
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    snippet = models.CharField(max_length=400, default='Add a snippet to display on blog index page')
    body = RichTextUploadingField(blank=True, null=True, config_name='special',)
    # body = models.TextField()
    # body = tinymce_models.HTMLField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='ML')
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | by ... ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))  # id is the same as pk
        return reverse('home') # redirect to home instead of the content of the post
