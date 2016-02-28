from rest_framework import viewsets

from restapi.models import Record
from restapi.serializers import RecordSerializer


class RecordViewSet(viewsets.ModelViewSet):
    """
    Provides a record view set.
    """

    #: Defines the queryset of the viewset.
    queryset = Record.objects.all()

    #: Defines the serializer class.
    serializer_class = RecordSerializer
