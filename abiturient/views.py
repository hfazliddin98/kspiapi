from rest_framework.viewsets import ModelViewSet
from .models import CallMarkaz, QabulHujjati, Bakalavr, Magistr
from .serialazer import CallMarkazSerializer, QabulHujjatiSerializer, BakalavrSerializer, MagistrSerializer


class CallMarkazViewSet(ModelViewSet):
    queryset = CallMarkaz.objects.all()
    serializer_class = CallMarkazSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


    

class QabulHujjatiViewSet(ModelViewSet):
    queryset = QabulHujjati.objects.all()
    serializer_class = QabulHujjatiSerializer
    http_method_names = ['get', 'post', 'put', 'delete']



class BakalavrViewSet(ModelViewSet):
    queryset = Bakalavr.objects.all()
    serializer_class = BakalavrSerializer
    http_method_names = ['get', 'post', 'put', 'delete']



class MagistrViewSet(ModelViewSet):
    queryset = Magistr.objects.all()
    serializer_class = MagistrSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


