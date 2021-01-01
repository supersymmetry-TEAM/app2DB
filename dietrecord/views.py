from rest_framework import viewsets
from rest_framework import permissions
from dietrecord.models import DietRecord
from rest_framework.response import Response
from rest_framework import status

from dietrecord.serializers import DietRecordSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
# class DietRecord(models.Model):
#     id = models.IntegerField(primary_key=True)
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     eat_date = models.CharField(max_length=500)
#     eat_time = models.CharField(max_length=500)
#     diet = models.ManyToManyField("nutfood.NutData", related_name="favs")
@api_view(["POST"])
def save_dieat(self, request):
    user = request.data.get('user',None)
    eat_date = request.data.get('eat_date',None)
    eat_time = request.data.get('eat_time',None)
    diet = request.data.get("diet",None)
    try:
        reco =DietRecord(user=user, eat_date=eat_date, eat_time=eat_time, diet=diet)
        reco.save()
        return Response(status=status.HTTP_200_OK)
    except ValueError:
        return Response({"messege":"Nodata"})


class DietRecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DietRecord.objects.all()
    serializer_class = DietRecordSerializer
    permission_classes = [permissions.IsAdminUser]