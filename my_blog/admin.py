from django.contrib import admin
from .models import User


# # Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    def gender(self):
        if self.gender:
            return "男"
        else:
            return "女"
    gender.short_description = "性别"

    def isDelete(self):
        if self.isDelete:
            return "已注销"
        else:
            return "活跃用户"
    isDelete.short_description = "是否删除"

    def username(self):
        return self.username
    username.short_description = "昵称"

    def password(self):
        return self.password
    password.short_description = "密码"

    def email(self):
        return self.email
    email.short_description = "邮箱"

    def birthday(self):
        return self.birthday
    birthday.short_description = "出生日期"

    def contend(self):
        return self.contend
    contend.short_description = "简介"

    def pk(self):
        return self.pk
    pk.short_description = "序号"

    list_display = [pk, username, gender, password, email, birthday, contend, isDelete]
    list_filter = ['username']
    search_fields = ['username']
    list_per_page = 20

    fieldsets = [
        ("昵称", {'fields': ['username']}),
        ('个人信息', {'fields': ['gender', 'password', 'email', 'birthday', 'contend']}),
    ]


