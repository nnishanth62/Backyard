from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
#from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse("post_detail", args=(str(self.id)))
        return reverse("home")  # returns to homepage


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #body = models.TextField()
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    snippet = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default="event")
    likes = models.ManyToManyField(User, related_name = 'blog_post')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse("post_detail", args=(str(self.id)))
        return reverse("home")  # returns to homepage
