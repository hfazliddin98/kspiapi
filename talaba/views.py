from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from  .models import TTJAriza, TTJCampus, TTJRahbar, TTJStatistika
from .models import TalabaBakalavr, TalabaMagistr
from .models import BakalavrMalakaTalabi, BakalavrOquvRejaTuri, BakalavrOquvReja, BakalavrFanDasturTuri, BakalavrFanDastur, BakalavrFanKatalogi
from .serialazer import TalabaBakalavrSerializer, TalabaMagistrSerializer
from .serialazer import BakalavrMalakaTalabiSerializer, BakalavrOquvRejaTuriSerializer, BakalavrOquvRejaSerializer
from .serialazer import BakalavrFanDasturTuriSerializer, BakalavrFanDasturSerializer, BakalavrFanKatalogiSerializer
from  .serialazer import TTJArizaSerializer, TTJCampusSerializer, TTJRahbarSerializer, TTJStatistikaSerializer




class TalabaBakalavrViewSet(ModelViewSet):
    queryset = TalabaBakalavr.objects.all()
    serializer_class = TalabaBakalavrSerializer


class TalabaMagistrViewSet(ModelViewSet):
    queryset = TalabaMagistr.objects.all()
    serializer_class = TalabaMagistrSerializer


class BakalavrMalakaTalabiViewSet(ModelViewSet):
    queryset = BakalavrMalakaTalabi.objects.all()
    serializer_class = BakalavrMalakaTalabiSerializer


class BakalavrOquvRejaTuriViewSet(ModelViewSet):
    queryset = BakalavrOquvRejaTuri.objects.all()
    serializer_class = BakalavrOquvRejaTuriSerializer


class BakalavrOquvRejaViewSet(ModelViewSet):
    queryset = BakalavrOquvReja.objects.all()
    serializer_class = BakalavrOquvRejaSerializer


class BakalavrFanDasturTuriViewSet(ModelViewSet):
    queryset = BakalavrFanDasturTuri.objects.all()
    serializer_class = BakalavrFanDasturTuriSerializer


class BakalavrFanDasturViewSet(ModelViewSet):
    queryset = BakalavrFanDastur.objects.all()
    serializer_class = BakalavrFanDasturSerializer


class BakalavrFanKatalogiViewSet(ModelViewSet):
    queryset = BakalavrFanKatalogi.objects.all()
    serializer_class = BakalavrFanKatalogiSerializer


# add

class TTJArizaViewSet(ModelViewSet):
    queryset = TTJAriza.objects.all()
    serializer_class = TTJArizaSerializer


class TTJCampusViewSet(ModelViewSet):
    queryset = TTJCampus.objects.all()
    serializer_class = TTJCampusSerializer


class TTJRahbarViewSet(ModelViewSet):
    queryset = TTJRahbar.objects.all()
    serializer_class = TTJRahbarSerializer


class TTJStatistikaViewSet(ModelViewSet):
    queryset = TTJStatistika.objects.all()
    serializer_class = TTJStatistikaSerializer

