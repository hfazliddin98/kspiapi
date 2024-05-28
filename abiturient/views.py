from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import CallMarkaz
from .serialazer import CallMarkazSerializer


class CallMarkazViewSet(ModelViewSet):
    queryset = CallMarkaz.objects.all()
    serializer_class = CallMarkazSerializer
    http_method_names = ['get', 'post', 'put', 'delete']