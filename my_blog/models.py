from django.db import models
from django.db.models import permalink


# Create your models here.
# 创建用户管理器
class UserManager(models.Manager):
    def createUser(self, username, gender, email, password, birthday, contend, isDelete=False):
        user = self.model()
        user.username = username
        user.gender = gender
        user.email = email
        user.password = password
        user.birthday  = birthday
        user.contend = contend
        return user


class User(models.Model):
    userobj = UserManager()
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


# 创建博客管理器
class BlogManager(models.Manager):
    def get_queryset(self):
        return super(BlogManager, self).get_queryset().filter(isDelete=False)

    def createBlog(self, title, postDate, slug, summary, body, author, isDelete=False):
        blog = self.model()
        blog.title = title
        blog.postDate = postDate
        blog.slug = slug
        blog.summary = summary
        blog.body = body
        blog.author = author
        return blog


class Blog(models.Model):
    blogobj = BlogManager()
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



