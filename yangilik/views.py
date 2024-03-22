from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Yangilik
from .serialazer import YangilikSerializer



class YangilikView(ListCreateAPIView):
   
    serializer_class = YangilikSerializer
    queryset = Yangilik.objects.all()
