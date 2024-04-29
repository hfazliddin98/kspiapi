from rest_framework.permissions import AllowAny # type: ignore
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView # type: ignore
from .models import Yangilik, Elon, GalareyaTuri, Galareya, Fikr, Talaba, Hamkorlarimiz, Statistika
from .serialazer import YangilikSerializer, ElonSerializer, GalareyaTuriSerializer, GalareyaSerializer, FikrSerializer, HamkorlarimizSerializer, TalabaSerializer, StatistikaSerializer


# yangilik 

class YangilikListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    metadata_class = Yangilik
    serializer_class = YangilikSerializer
    queryset = Yangilik.objects.all()

class YangilikRetrieveAPIView(RetrieveAPIView):
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


# elon 
    
class ElonListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    metadata_class = Elon
    serializer_class = ElonSerializer
    queryset = Elon.objects.all()

class ElonRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    metadata_class = Elon
    serializer_class = ElonSerializer
    queryset = Elon.objects.all()

class ElonCreateAPIView(CreateAPIView):
    metadata_class = Elon
    serializer_class = ElonSerializer
    queryset = Elon.objects.all()

class ElonUpdateAPIView(UpdateAPIView):
    metadata_class = Elon
    serializer_class = ElonSerializer
    queryset = Elon.objects.all()

class ElonDestroyAPIView(DestroyAPIView):
    metadata_class = Elon
    serializer_class = ElonSerializer
    queryset = Elon.objects.all()


# galareya turi

class GalareyaTuriListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    metadata_class = GalareyaTuri
    serializer_class = GalareyaTuriSerializer
    queryset = GalareyaTuri.objects.all()

class GalareyaTuriRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    metadata_class = GalareyaTuri
    serializer_class = GalareyaTuriSerializer
    queryset = GalareyaTuri.objects.all()

class GalareyaTuriCreateAPIView(CreateAPIView):
    metadata_class = GalareyaTuri
    serializer_class = GalareyaTuriSerializer
    queryset = GalareyaTuri.objects.all()

class GalareyaTuriUpdateAPIView(UpdateAPIView):
    metadata_class = GalareyaTuri
    serializer_class = GalareyaTuriSerializer
    queryset = GalareyaTuri.objects.all()

class GalareyaTuriDestroyAPIView(DestroyAPIView):
    metadata_class = GalareyaTuri
    serializer_class = GalareyaTuriSerializer
    queryset = GalareyaTuri.objects.all()



# galareya

class GalareyaListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    metadata_class = Galareya
    serializer_class = GalareyaSerializer
    queryset = Galareya.objects.all()

class GalareyaRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    metadata_class = Galareya
    serializer_class = GalareyaSerializer
    queryset = Galareya.objects.all()

class GalareyaCreateAPIView(CreateAPIView):
    metadata_class = Galareya
    serializer_class = GalareyaSerializer
    queryset = Galareya.objects.all()

class GalareyaUpdateAPIView(UpdateAPIView):
    metadata_class = Galareya
    serializer_class = GalareyaSerializer
    queryset = Galareya.objects.all()

class GalareyaDestroyAPIView(DestroyAPIView):
    metadata_class = Galareya
    serializer_class = GalareyaSerializer
    queryset = Galareya.objects.all()




# fikr

class FikrListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    metadata_class = Fikr
    serializer_class = FikrSerializer
    queryset = Fikr.objects.all()

class FikrRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    metadata_class = Fikr
    serializer_class = FikrSerializer
    queryset = Fikr.objects.all()

class FikrCreateAPIView(CreateAPIView):
    metadata_class = Fikr
    serializer_class = FikrSerializer
    queryset = Fikr.objects.all()

class FikrUpdateAPIView(UpdateAPIView):
    metadata_class = Fikr
    serializer_class = FikrSerializer
    queryset = Fikr.objects.all()

class FikrDestroyAPIView(DestroyAPIView):
    metadata_class = Fikr
    serializer_class = FikrSerializer
    queryset = Fikr.objects.all()



# hamkor

class HamkorlarimizListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    metadata_class = Hamkorlarimiz
    serializer_class = HamkorlarimizSerializer
    queryset = Hamkorlarimiz.objects.all()

class HamkorlarimizRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    metadata_class = Hamkorlarimiz
    serializer_class = HamkorlarimizSerializer
    queryset = Hamkorlarimiz.objects.all()

class HamkorlarimizCreateAPIView(CreateAPIView):
    metadata_class = Hamkorlarimiz
    serializer_class = HamkorlarimizSerializer
    queryset = Hamkorlarimiz.objects.all()

class HamkorlarimizUpdateAPIView(UpdateAPIView):
    metadata_class = Hamkorlarimiz
    serializer_class = HamkorlarimizSerializer
    queryset = Hamkorlarimiz.objects.all()

class HamkorlarimizDestroyAPIView(DestroyAPIView):
    metadata_class = Hamkorlarimiz
    serializer_class = HamkorlarimizSerializer
    queryset = Hamkorlarimiz.objects.all()

# statistika

class StatistikaListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    metadata_class = Statistika
    serializer_class = StatistikaSerializer
    queryset = Statistika.objects.all()

class StatistikaRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    metadata_class = Statistika
    serializer_class = StatistikaSerializer
    queryset = Statistika.objects.all()

class StatistikaCreateAPIView(CreateAPIView):
    metadata_class = Statistika
    serializer_class = StatistikaSerializer
    queryset = Statistika.objects.all()

class StatistikaUpdateAPIView(UpdateAPIView):
    metadata_class = Statistika
    serializer_class = StatistikaSerializer
    queryset = Statistika.objects.all()

class StatistikaDestroyAPIView(DestroyAPIView):
    metadata_class = Statistika
    serializer_class = StatistikaSerializer
    queryset = Statistika.objects.all()

# talaba

class TalabaListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    metadata_class = Talaba
    serializer_class = TalabaSerializer
    queryset = Talaba.objects.all()

class TalabaRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    metadata_class = Talaba
    serializer_class = TalabaSerializer
    queryset = Talaba.objects.all()

class TalabaCreateAPIView(CreateAPIView):
    metadata_class = Talaba
    serializer_class = TalabaSerializer
    queryset = Talaba.objects.all()

class TalabaUpdateAPIView(UpdateAPIView):
    metadata_class = Talaba
    serializer_class = TalabaSerializer
    queryset = Talaba.objects.all()

class TalabaDestroyAPIView(DestroyAPIView):
    metadata_class = Talaba
    serializer_class = TalabaSerializer
    queryset = Talaba.objects.all()

