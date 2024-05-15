from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import AllowAny # type: ignore
from .models import Yangilik, Elon, GalareyaTuri, Galareya, Fikr, Talaba, Hamkorlarimiz, Statistika, ElektronKutubxona, MasofaviyTalim, VirtualQabulxona, VideoMaruzalar, Fakultet
from .serialazer import YangilikSerializer, ElonSerializer, GalareyaTuriSerializer, GalareyaSerializer, FikrSerializer, HamkorlarimizSerializer, TalabaSerializer
from .serialazer import ElektronKutubxonaSerializer, VirtualQabulxonaSerializer, VideoMaruzalarSerializer, MasofaviyTalimSerializer, StatistikaSerializer, FakultetSerializer


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
    queryset = VirtualQabulxona.objects.all()
    serializer_class = VirtualQabulxonaSerializer


class FakultetViewSet(ModelViewSet):
    queryset = Fakultet.objects.all()
    serializer_class = FakultetSerializer



