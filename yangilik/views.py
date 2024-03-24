from rest_framework.generics import ListCreateAPIView
from .models import Yangilik, Sinov, Malumot
from .serialazer import YangilikSerializer, SinovSerializer, MalumotSerializer



class YangilikView(ListCreateAPIView):
    metadata_class = Yangilik
    serializer_class = YangilikSerializer
    queryset = Yangilik.objects.all()

class SinovView(ListCreateAPIView):
    metadata_class = Sinov
    serializer_class = SinovSerializer
    queryset = Sinov.objects.all()


class MalumotView(ListCreateAPIView):
    metadata_class = Malumot
    serializer_class = MalumotSerializer
    queryset = Malumot.objects.all()