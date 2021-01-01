from django.urls import path
from dietrecord.views import DietRecordViewSet
app_name = "dietrecord"

urlpatterns = [
    path("search_nut/", DietRecordViewSet),
  ]