from django.shortcuts import render, redirect
from .models import User, Blog
from .forms.forms import RegisterForm, BlogForm


# Create your views here.
def login(request):
    return render(request, "my_blog/login.html")


def index(request):
    if request.method == "POST":
        username = request.POST.get("username")
        if not username:
            return render(request, "my_blog/login.html")
        if not User.userobj.get_queryset().filter(username=username):
            return render(request, "my_blog/login.html", {"msg": "用户名不存在"})
        password = request.POST.get("password")
        if password == User.userobj.get(username=username).password:
            return redirect("/" + username + "/")
        else:
            return render(request, "my_blog/login.html", {"msg": "密码错误"})
    return render(request, "my_blog/login.html")


def blog(request, username):
    author = User.userobj.filter(username=username).values("pk")
    authorid = 0
    for i in author:
        authorid = i["pk"]
    blogs = Blog.blogobj.get_queryset().filter(author_id=authorid)
    return render(request, 'my_blog/blog.html', {"blogs":blogs})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            if User.userobj.get_queryset().filter(username=username):
                return render(request, "my_blog/register.html", {"form": form, "msg1": "用户名已注册"})
            gender = form.cleaned_data["gender"]
            email = form.cleaned_data['email']
            birthday = form.cleaned_data['birthday']
            password = form.cleaned_data["password"]
            reptpassword = form.cleaned_data["reptpassword"]
            if password != reptpassword:
                return render(request, "my_blog/register.html", {"form": form, "msg2": "两次密码输入不同"})
            contend = form.cleaned_data['contend']
            newUser = User.userobj.createUser(username, gender, email, password, birthday, contend)
            newUser.save()
            return redirect('/login/')
    else:
        form = RegisterForm()
    return render(request, 'my_blog/register.html', {'form': form})


def newBlog(request, author):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            authors = User.userobj.get_queryset().filter(username=author)
            for i in authors:
                author = i
            summary = form.cleaned_data["summary"]
            body = request.POST.get("body")
            newblog = Blog.blogobj.createBlog(title, summary, body, author)
            newblog.save()
            author = User.userobj.filter(username=author).values("username")
            username = 0
            for i in author:
                username = i["username"]
            return redirect("/" + username + "/")
        else:
            form = BlogForm()
        return render(request, "my_blog/newblog.html", {"form": form})
    else:
        form = BlogForm()
    return render(request, "my_blog/newblog.html", {"form": form})



