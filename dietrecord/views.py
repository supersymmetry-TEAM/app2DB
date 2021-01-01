from rest_framework import viewsets
from rest_framework import permissions
from dietrecord.models import DietRecord
from dietrecord.serializers import DietRecordSerializer


class DietRecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DietRecord.objects.all()
    serializer_class = DietRecordSerializer
    permission_classes = [permissions.IsAdminUser]