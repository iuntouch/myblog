from django.db import models
from django.db.models import permalink


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    gender = models.BooleanField(default=True)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    birthday = models.DateField()
    contend = models.CharField(max_length=40)
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = "users"
        ordering = ["id"]

    def __str__(self):
        return self.username


class Blog(models.Model):
    title = models.CharField(max_length=100)
    postDate = models.DateTimeField()
    slug = models.SlugField(max_length=100)
    summary = models.CharField(max_length=150)
    body = models.TextField()
    isDelete = models.BooleanField(default=False)
    author = models.ForeignKey("User", on_delete=models.CASCADE)

    class Meta:
        db_table = "blogs"
        ordering = ["id"]

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, {'slug' : self.slug})



