from django.db import models
from nutfood.models import NutData 
from users.models import User

class DietRecord(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    eat_date = models.CharField(max_length=500)
    eat_time = models.CharField(max_length=500)
    diet = models.ManyToManyField("nutfood.NutData", related_name="favs")

