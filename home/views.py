from rest_framework.permissions import AllowAny
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Yangilik, Elon, GalareyaTuri, Galareya
from .serialazer import YangilikSerializer, ElonSerializer, GalareyaTuriSerializer, GalareyaSerializer



class YangilikListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    metadata_class = Yangilik
    serializer_class = YangilikSerializer
    queryset = Yangilik.objects.all()


class YangilikCreateAPIView(CreateAPIView):
    metadata_class = Yangilik
    serializer_class = YangilikSerializer
    queryset = Yangilik.objects.all()

class YangilikUpdateAPIView(UpdateAPIView):
    metadata_class = Yangilik
    serializer_class = YangilikSerializer
    queryset = Yangilik.objects.all()


class YangilikDestroyAPIView(DestroyAPIView):
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

