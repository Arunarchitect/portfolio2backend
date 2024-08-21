from django.urls import path
from .views import AboutViewSet

urlpatterns = [
    path('list/', AboutViewSet.as_view({'get': 'list'}), name='list'),
]
