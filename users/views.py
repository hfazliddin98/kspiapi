from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework import filters
from home.models import Yangilik, Elon
from .serialazer import YangilikSearchSerializer, ElonSearchSerializer

def bosh_sahifa(request):
    return redirect('/swagger/')

class YangilikSearchView(generics.ListAPIView):
    queryset = Yangilik.objects.all()
    serializer_class = YangilikSearchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title_uz', 'title_ru', 'title_en']


class ElonSearchView(generics.ListAPIView):
    queryset = Elon.objects.all()
    serializer_class = ElonSearchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title_uz', 'title_ru', 'title_en']