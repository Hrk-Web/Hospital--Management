from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserMobData(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mob_no = models.CharField(max_length=10, unique=True, default="000")
    username = models.CharField(max_length=50, default="no name")

    def __str__(self):
        return self.username   # username is string type that's why converion didn't take place here.

