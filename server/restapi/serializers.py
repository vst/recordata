from rest_framework import serializers

from restapi.models import Record


class RecordSerializer(serializers.ModelSerializer):
    """
    Provides a record serializer.
    """

    class Meta:
        model = Record
        fields = ["id", "key", "value"]
        read_only_fields = ["id"]
