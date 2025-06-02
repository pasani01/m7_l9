from django.urls import path

from .views import dictionary_list, dictionary_detail



urlpatterns = [
    path('list/',dictionary_list,name='dict-list'),
    path('detail',dictionary_detail,name='dict-detail'),
]

