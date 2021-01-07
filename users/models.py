from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


class User(User):
    avatar = models.ImageField(upload_to="avatars", blank=True)
    # favs = models.ManyToManyField("nutfood.NutData", related_name="favs")