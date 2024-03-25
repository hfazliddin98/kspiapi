from rest_framework.generics import ListCreateAPIView
from .models import Yangilik, Elon
from .serialazer import YangilikSerializer, ElonSerializer



class YangilikView(ListCreateAPIView):
    metadata_class = Yangilik
    serializer_class = YangilikSerializer
    queryset = Yangilik.objects.all()


class ElonView(ListCreateAPIView):
    metadata_class = Elon
    serializer_class = ElonSerializer
    queryset = Elon.objects.all()

