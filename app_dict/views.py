from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, filters
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Dictionary
from .serializers import DictListSerializer
from .pagenations import DictPagination



@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter(
            'search', openapi.IN_QUERY, description="Search query for fields: word_ru, word_uz_k, word_uz_l, word_en, word_tr, catagory__catagory_name",
            type=openapi.TYPE_STRING
        ),
        openapi.Parameter(
            'ordering', openapi.IN_QUERY, description="Order by fields: field1, field2 (e.g., ?ordering=field1 or ?ordering=-field2)",
            type=openapi.TYPE_STRING
        ),
        openapi.Parameter(
            'page', openapi.IN_QUERY, description="Page number for pagination", type=openapi.TYPE_INTEGER
        ),
        openapi.Parameter(
            'page_size', openapi.IN_QUERY, description="Number of results per page", type=openapi.TYPE_INTEGER
        ),
    ]
)
@api_view(['GET', 'POST'])
def dictionary_list(request):
    if request.method == 'GET':
        dictionaries = Dictionary.objects.all()

        search_query = request.query_params.get('search', None)
        if search_query:
            dictionaries = dictionaries.filter(
                Q(word_ru__icontains=search_query) |
                Q(word_uz_k__icontains=search_query) |
                Q(word_uz_l__icontains=search_query) |
                Q(word_en__icontains=search_query) |
                Q(word_tr__icontains=search_query) |
                Q(catagory__catagory_name__icontains=search_query)
            )

        ordering = request.query_params.get('ordering', None)
        if ordering:
            dictionaries = dictionaries.order_by(ordering)

        paginator = DictPagination()
        result_page = paginator.paginate_queryset(dictionaries, request)
        serializer = DictListSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = DictListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='get', responses={200: DictListSerializer})
@swagger_auto_schema(method='put', request_body=DictListSerializer, responses={200: DictListSerializer})
@swagger_auto_schema(method='delete', responses={204: 'No Content'})
@api_view(['GET', 'PUT', 'DELETE'])
def dictionary_detail(request, id):
    try:
        dictionary = Dictionary.objects.get(id=id)
    except Dictionary.DoesNotExist:
        return Response({'error': 'Dictionary not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DictListSerializer(dictionary)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DictListSerializer(dictionary, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        dictionary.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
