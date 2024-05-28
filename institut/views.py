from rest_framework.viewsets import ModelViewSet
from .models import InstitutHaqida, InstitutMalumotlari, Kengash, Tuzilma,InstitutRekviziti, BankRekviziti, Qabulxona
from .serialazer import InstitutHaqidaSerializer, InstitutMalumotlariSerializer, KengashSerializer, TuzilmaSerializer
from .serialazer import InstitutRekvizitiSerializer, BankRekvizitiSerializer, QabulxonaSerializer




class InstitutHaqidaViewSet(ModelViewSet):
    queryset = InstitutHaqida.objects.all()
    serializer_class = InstitutHaqidaSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    

class InstitutMalumotlariViewSet(ModelViewSet):
    queryset = InstitutMalumotlari.objects.all()
    serializer_class = InstitutMalumotlariSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    
class KengashViewSet(ModelViewSet):
    queryset = Kengash.objects.all()
    serializer_class = KengashSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    

class TuzilmaViewSet(ModelViewSet):
    queryset = Tuzilma.objects.all()
    serializer_class = TuzilmaSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    

class InstitutRekvizitiViewSet(ModelViewSet):
    queryset = InstitutRekviziti.objects.all()
    serializer_class = InstitutRekvizitiSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    

class BankRekvizitiViewSet(ModelViewSet):
    queryset = BankRekviziti.objects.all()
    serializer_class = BankRekvizitiSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class QabulxonaViewSet(ModelViewSet):
    queryset = Qabulxona.objects.all()
    serializer_class = QabulxonaSerializer
    http_method_names = ['get', 'post']
