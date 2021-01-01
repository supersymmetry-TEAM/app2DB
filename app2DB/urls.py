from django.urls import include, path
from rest_framework import routers
from nutfood import views
from django.contrib import admin

urlpatterns = [
    path("nutfood/", include("nutfood.urls")),
    path("admin/", admin.site.urls),
    # path("usrs/v1/", include("users.urls")),
]