from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .models import NutData
from nutfood.serializers import NutDataSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.response import Response
from django.db.models import Count
from nutfood.models import NutData
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser, AllowAny
class OwnPagination(PageNumberPagination):
    page_size = 20

@api_view(["GET"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated]) 
def food_of_nut_search(request):
    paginator = OwnPagination()
    pd_name = request.GET.get("pd_name", None)
    # pd_name_nospace = pd_name.replace(" ","")
    filter_kwargs = {}
    if pd_name is not None:
        filter_kwargs["DESC_KOR__icontains"] = pd_name
    try:
        foods = NutData.objects.filter(**filter_kwargs).order_by('-SEARCH_SCORE','DESC_KOR')
    except ValueError:
        foods = NutData.objects.all()
    results = paginator.paginate_queryset(foods, request)
    serializer = NutDataSerializer(results, many=True,context={"request": request})
    return paginator.get_paginated_response(serializer.data)

