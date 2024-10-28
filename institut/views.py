from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import InstitutHaqida, InstitutMalumotlari, Kengash, Tuzilma,InstitutRekviziti, BankRekviziti, Qabulxona
from .models import KorupsiyagaXabar
from .serialazer import InstitutHaqidaSerializer, InstitutMalumotlariSerializer, KengashSerializer, TuzilmaSerializer
from .serialazer import InstitutRekvizitiSerializer, BankRekvizitiSerializer, QabulxonaSerializer, KorupsiyagaXabarSerializer




class InstitutHaqidaViewSet(ModelViewSet):
    queryset = InstitutHaqida.objects.all()
    serializer_class = InstitutHaqidaSerializer


class InstitutMalumotlariViewSet(ModelViewSet):
    queryset = InstitutMalumotlari.objects.all()
    serializer_class = InstitutMalumotlariSerializer

class KengashViewSet(ModelViewSet):
    queryset = Kengash.objects.all()
    serializer_class = KengashSerializer


class TuzilmaViewSet(ModelViewSet):
    queryset = Tuzilma.objects.all()
    serializer_class = TuzilmaSerializer


class InstitutRekvizitiViewSet(ModelViewSet):
    queryset = InstitutRekviziti.objects.all()
    serializer_class = InstitutRekvizitiSerializer


class BankRekvizitiViewSet(ModelViewSet):
    queryset = BankRekviziti.objects.all()
    serializer_class = BankRekvizitiSerializer


class QabulxonaViewSet(ModelViewSet):
    queryset = Qabulxona.objects.all()
    serializer_class = QabulxonaSerializer
    permission_classes = [AllowAny]


class KorupsiyagaXabarViewSet(ModelViewSet):
    queryset = KorupsiyagaXabar.objects.all()
    serializer_class = KorupsiyagaXabarSerializer
    permission_classes = [AllowAny]


