from rest_framework.viewsets import ModelViewSet

from .models import Dictionary
from .serializers import DictListSerializer


class DictViewSet(ModelViewSet):
    queryset=Dictionary.objects.all()
    lookup_field='id'
    def get_serializer_class(self):
        return DictListSerializer