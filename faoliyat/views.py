from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Jamoatchilik, Madaniy, Oquv, Akademik, Ilmiy, Yoshlar
from .serialazer import JamoatchilikSerializer, MadaniySerializer, OquvSerializer, AkademikSerializer, IlmiySerializer, YoshlarSerializer



class JamoatchilikViewSet(ModelViewSet):
    queryset = Jamoatchilik.objects.all()
    serializer_class = JamoatchilikSerializer


class MadaniyViewSet(ModelViewSet):
    queryset = Madaniy.objects.all()
    serializer_class = MadaniySerializer


class OquvViewSet(ModelViewSet):
    queryset = Oquv.objects.all()
    serializer_class = OquvSerializer


class AkademikViewSet(ModelViewSet):
    queryset = Akademik.objects.all()
    serializer_class = AkademikSerializer


class IlmiyViewSet(ModelViewSet):
    queryset = Ilmiy.objects.all()
    serializer_class = IlmiySerializer


class YoshlarViewSet(ModelViewSet):
    queryset = Yoshlar.objects.all()
    serializer_class = YoshlarSerializer

