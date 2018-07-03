from django.shortcuts import render, redirect
from .models import User, Blog
from django.http import HttpResponse
from django.contrib.auth import logout


# Create your views here.
def index(request):
    return render(request, "my_blog/index.html")


def blog(request, username):
    authorid = User.userobj.get(username=username).pk
    blogs = Blog.blogobj.get_queryset().filter(author_id=authorid)
    return render(request, 'my_blog/blog.html', {"blogs": blogs})


def register(request):
    return render(request, 'my_blog/register.html')



