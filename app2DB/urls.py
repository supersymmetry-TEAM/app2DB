from django.urls import include, path
from rest_framework import routers
from nutfood import views
from django.contrib import admin
from dietrecord import views
urlpatterns = [
    path("nutfood/", include("nutfood.urls")),
    path("admin/", admin.site.urls),
    path("usr_day_dietrecord/", include("dietrecord.urls")),
]