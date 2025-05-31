from rest_framework.serializers import SerializerMethodField ,ModelSerializer

from .models import Dictionary

class DictListSerializer(ModelSerializer):
    class Meta:
        model=Dictionary
        fields='__all__'
        read_only_fields=('id',)
