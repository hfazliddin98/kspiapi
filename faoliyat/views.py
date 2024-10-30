from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Jamoatchilik, Madaniy, Oquv, Akademik, Ilmiy, Yoshlar, NormativHujatlar, IchkiIdoraviyHujatlar, XabarBerish
from .models import XalqaroProfesorlarFikri, XalqaroHamkorlar
from .serialazer import JamoatchilikSerializer, MadaniySerializer, OquvSerializer, AkademikSerializer, IlmiySerializer, YoshlarSerializer
from .serialazer import NormativHujatlarSerializer, IchkiIdoraviyHujatlarSerializer, XabarBerishSerializer
from .serialazer import XalqaroProfesorlarFikriSerializer, XalqaroHamkorlarSerializer



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


class NormativHujatlarViewSet(ModelViewSet):
    queryset = NormativHujatlar.objects.all()
    serializer_class = NormativHujatlarSerializer


class IchkiIdoraviyHujatlarViewSet(ModelViewSet):
    queryset = IchkiIdoraviyHujatlar.objects.all()
    serializer_class = IchkiIdoraviyHujatlarSerializer


class XabarBerishViewSet(ModelViewSet):
    queryset = XabarBerish.objects.all()
    serializer_class = XabarBerishSerializer


class XalqaroProfesorlarFikriViewSet(ModelViewSet):
    queryset = XalqaroProfesorlarFikri.objects.all()
    serializer_class = XalqaroProfesorlarFikriSerializer


class XalqaroHamkorlarViewSet(ModelViewSet):
    queryset = XalqaroHamkorlar.objects.all()
    serializer_class = XalqaroHamkorlarSerializer

