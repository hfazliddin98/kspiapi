from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from  .models import TTJAriza, TTJCampus, TTJRahbar, TTJStatistika
from .models import TalabaBakalavr, TalabaMagistr
from .models import BakalavrMalakaTalabi, BakalavrOquvRejaTuri, BakalavrOquvReja, BakalavrFanDasturTuri, BakalavrFanDastur, BakalavrFanKatalogi
from .models import BakalavrFanDasturKurs, BakalavrFanDasturYonalish, BakalavrFanDasturTalimTuri
from .models import MagistrMalakaTalabi, MagistrOquvRejaTuri, MagistrOquvReja, MagistrFanDasturTuri, MagistrFanDastur, MagistrFanKatalogi
from .models import MagistrFanDasturKurs, MagistrFanDasturYonalish
from .serialazer import TalabaBakalavrSerializer, TalabaMagistrSerializer
from .serialazer import BakalavrMalakaTalabiSerializer, BakalavrOquvRejaTuriSerializer, BakalavrOquvRejaSerializer
from .serialazer import BakalavrFanDasturTuriSerializer, BakalavrFanDasturSerializer, BakalavrFanKatalogiSerializer
from .serialazer import BakalavrFanDasturKursSerializer, BakalavrFanDasturYonalishSerializer, BakalavrFanDasturTalimTuriSerializer
from .serialazer import MagistrMalakaTalabiSerializer, MagistrOquvRejaTuriSerializer, MagistrOquvRejaSerializer
from .serialazer import MagistrFanDasturTuriSerializer, MagistrFanDasturSerializer, MagistrFanKatalogiSerializer
from .serialazer import MagistrFanDasturKursSerializer, MagistrFanDasturYonalishSerializer
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


class BakalavrFanDasturKursViewSet(ModelViewSet):
    queryset = BakalavrFanDasturKurs.objects.all()
    serializer_class = BakalavrFanDasturKursSerializer


class BakalavrFanDasturTalimTuriViewSet(ModelViewSet):
    queryset = BakalavrFanDasturTalimTuri.objects.all()
    serializer_class = BakalavrFanDasturTalimTuriSerializer


class BakalavrFanDasturYonalishViewSet(ModelViewSet):
    queryset = BakalavrFanDasturYonalish.objects.all()
    serializer_class = BakalavrFanDasturYonalishSerializer


class BakalavrFanDasturTuriViewSet(ModelViewSet):
    queryset = BakalavrFanDasturTuri.objects.all()
    serializer_class = BakalavrFanDasturTuriSerializer


class BakalavrFanDasturViewSet(ModelViewSet):
    queryset = BakalavrFanDastur.objects.all()
    serializer_class = BakalavrFanDasturSerializer


class BakalavrFanKatalogiViewSet(ModelViewSet):
    queryset = BakalavrFanKatalogi.objects.all()
    serializer_class = BakalavrFanKatalogiSerializer





class MagistrMalakaTalabiViewSet(ModelViewSet):
    queryset = MagistrMalakaTalabi.objects.all()
    serializer_class = MagistrMalakaTalabiSerializer


class MagistrOquvRejaTuriViewSet(ModelViewSet):
    queryset = MagistrOquvRejaTuri.objects.all()
    serializer_class = MagistrOquvRejaTuriSerializer


class MagistrOquvRejaViewSet(ModelViewSet):
    queryset = MagistrOquvReja.objects.all()
    serializer_class = MagistrOquvRejaSerializer


class MagistrFanDasturKursViewSet(ModelViewSet):
    queryset = MagistrFanDasturKurs.objects.all()
    serializer_class = MagistrFanDasturKursSerializer


class MagistrFanDasturYonalishViewSet(ModelViewSet):
    queryset = MagistrFanDasturYonalish.objects.all()
    serializer_class = MagistrFanDasturYonalishSerializer


class MagistrFanDasturTuriViewSet(ModelViewSet):
    queryset = MagistrFanDasturTuri.objects.all()
    serializer_class = MagistrFanDasturTuriSerializer


class MagistrFanDasturViewSet(ModelViewSet):
    queryset = MagistrFanDastur.objects.all()
    serializer_class = MagistrFanDasturSerializer


class MagistrFanKatalogiViewSet(ModelViewSet):
    queryset = MagistrFanKatalogi.objects.all()
    serializer_class = MagistrFanKatalogiSerializer





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

