from django.urls import path
from nutfood.views import food_of_nut_search
app_name = "nutfood"

urlpatterns = [
    path("search_nut/", food_of_nut_search),
  ]