from django.db import models


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

