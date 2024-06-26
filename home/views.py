from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .models import Yangilik, Elon, GalareyaTuri, Galareya, Fikr, Talaba, Hamkorlarimiz, Statistika, ElektronKutubxona, MasofaviyTalim, VirtualQabulxona, VideoMaruzalar, Boglanish
from .models import Vakansiya, EfirName, Efir
from .serialazer import YangilikSerializer, ElonSerializer, GalareyaTuriSerializer, GalareyaSerializer, FikrSerializer, HamkorlarimizSerializer, TalabaSerializer
from .serialazer import ElektronKutubxonaSerializer, VirtualQabulxonaSerializer, VideoMaruzalarSerializer, MasofaviyTalimSerializer, StatistikaSerializer
from .serialazer import BoglanishSerializer, VakansiyaSerializer, EfirNameSerializer, EfirSerializer



class YangilikViewSet(ModelViewSet):
    queryset = Yangilik.objects.all()
    serializer_class = YangilikSerializer



class ElonViewSet(ModelViewSet):
    queryset = Elon.objects.all()
    serializer_class = ElonSerializer



class GalareyaTuriViewSet(ModelViewSet):
    queryset = GalareyaTuri.objects.all()
    serializer_class = GalareyaTuriSerializer



class GalareyaViewSet(ModelViewSet):
    queryset = Galareya.objects.all()
    serializer_class = GalareyaSerializer



class FikrViewSet(ModelViewSet):
    queryset = Fikr.objects.all()
    serializer_class = FikrSerializer



class HamkorlarimizViewSet(ModelViewSet):
    queryset = Hamkorlarimiz.objects.all()
    serializer_class = HamkorlarimizSerializer



class StatistikaViewSet(ModelViewSet):
    queryset = Statistika.objects.all()
    serializer_class = StatistikaSerializer



class TalabaViewSet(ModelViewSet):
    queryset = Talaba.objects.all()
    serializer_class = TalabaSerializer



class ElektronKutubxonaViewSet(ModelViewSet):
    queryset = ElektronKutubxona.objects.all()
    serializer_class = ElektronKutubxonaSerializer



class MasofaviyTalimViewSet(ModelViewSet):
    queryset = MasofaviyTalim.objects.all()
    serializer_class = MasofaviyTalimSerializer



class VideoMaruzalarViewSet(ModelViewSet):
    queryset = VideoMaruzalar.objects.all()
    serializer_class = VideoMaruzalarSerializer



class VirtualQabulxonaViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = VirtualQabulxona.objects.all()
    serializer_class = VirtualQabulxonaSerializer



class BoglanishViewSet(ModelViewSet):
    queryset = Boglanish.objects.all()
    serializer_class = BoglanishSerializer


class VakansiyaViewSet(ModelViewSet):
    queryset = Vakansiya.objects.all()
    serializer_class = VakansiyaSerializer


class EfirNameViewSet(ModelViewSet):
    queryset = EfirName.objects.all()
    serializer_class = EfirNameSerializer


class EfirViewSet(ModelViewSet):
    queryset = Efir.objects.all()
    serializer_class = EfirSerializer




