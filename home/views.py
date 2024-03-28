from rest_framework.generics import ListCreateAPIView
from .models import Yangilik, Elon, GalareyaTuri, Galareya
from .serialazer import YangilikSerializer, ElonSerializer, GalareyaTuriSerializer, GalareyaSerializer



class YangilikView(ListCreateAPIView):
    metadata_class = Yangilik
    serializer_class = YangilikSerializer
    queryset = Yangilik.objects.all()


class ElonView(ListCreateAPIView):
    metadata_class = Elon
    serializer_class = ElonSerializer
    queryset = Elon.objects.all()


class GalareyaTuriView(ListCreateAPIView):
    metadata_class = GalareyaTuri
    serializer_class = GalareyaTuriSerializer
    queryset = GalareyaTuri.objects.all()


class GalareyaView(ListCreateAPIView):
    metadata_class = Galareya
    serializer_class = GalareyaSerializer
    queryset = Galareya.objects.all()

