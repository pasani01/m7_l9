from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from .models import Dictionary
from .serializers import DictListSerializer
from .pagenations import DictPagination

class DictViewSet(ModelViewSet):
    queryset = Dictionary.objects.all()
    lookup_field = 'id'
    serializer_class = DictListSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['word_ru', 'word_uz_k', 'word_uz_l', 'word_en', 'word_tr', 'catagory__catagory_name']
    ordering_fields = ['field1', 'field2']  

    pagination_class = DictPagination

    def get_serializer_class(self):
        return DictListSerializer