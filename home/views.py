from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
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

class YangilikRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    metadata_class = Yangilik
    serializer_class = YangilikSerializer
    queryset = Yangilik.objects.all()


# elon 
    
class ElonListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    metadata_class = Elon
    serializer_class = ElonSerializer
    queryset = Elon.objects.all()


class ElonCreateAPIView(CreateAPIView):
    metadata_class = Elon
    serializer_class = ElonSerializer
    queryset = Elon.objects.all()

class ElonRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    metadata_class = Elon
    serializer_class = ElonSerializer
    queryset = Elon.objects.all()


# galareya turi

class GalareyaTuriListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    metadata_class = GalareyaTuri
    serializer_class = GalareyaTuriSerializer
    queryset = GalareyaTuri.objects.all()


class GalareyaTuriCreateAPIView(CreateAPIView):
    metadata_class = GalareyaTuri
    serializer_class = GalareyaTuriSerializer
    queryset = GalareyaTuri.objects.all()

class GalareyaTuriRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    metadata_class = GalareyaTuri
    serializer_class = GalareyaTuriSerializer
    queryset = GalareyaTuri.objects.all()

# galareya

class GalareyaListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    metadata_class = Galareya
    serializer_class = GalareyaSerializer
    queryset = Galareya.objects.all()


class GalareyaCreateAPIView(CreateAPIView):
    metadata_class = Galareya
    serializer_class = GalareyaSerializer
    queryset = Galareya.objects.all()

class GalareyaRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    metadata_class = Galareya
    serializer_class = GalareyaSerializer
    queryset = Galareya.objects.all()



