from rest_framework.routers import DefaultRouter

from .views import DictViewSet


roter=DefaultRouter()

roter.register('',DictViewSet,basename="dict")

urlpatterns = [
    
]

urlpatterns+=roter.urls