# -*- coding: utf-8 -*-
# @ProjectName  : myblog
# @Time    : 2018/7/5 11:19
# @Author  : CHEN HUI   @iuntouch
# @Email   : huch7280@tju.edu.cn
# @File    : forms.py
# @Software: PyCharm


from django import forms
from ..models import User
from tinymce.models import HTMLField


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, required=True, error_messages={"0": "用户名已注册"})
    gender = forms.ChoiceField(required=True, choices=((1, "男"), (0, "女")), initial=1, widget=forms.RadioSelect)
    email = forms.EmailField(max_length=30, required=True)
    password = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput)
    reptpassword = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput)
    birthday = forms.DateField(required=True)
    contend = forms.CharField(max_length=40)

    def checkpassword(self):
        password = self.cleaned_data["password"]
        reptpassword = self.cleaned_data["reptpassword"]
        if password != reptpassword:
            return False
        return True

    def checkusername(self):
        try:
            username = self.cleaned_data["username"]
        finally:
            usernames = list(User.userobj.get_queryset().values_list("username"))
            for user in usernames:
                if username in user:
                    return False
            return True


class BlogForm(forms.Form):
    title = forms.CharField(max_length=100)
    summary = forms.CharField(max_length=150)
    body = HTMLField()
    author = forms.CharField(max_length=20)
