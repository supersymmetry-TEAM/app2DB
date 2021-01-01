from django.urls import path
from dietrecord.views import DietRecordViewSet, save_dieat
app_name = "dietrecord"

urlpatterns = [
    path("search_nut/", DietRecordViewSet),
    path("save_dieat/", save_dieat),
  ]