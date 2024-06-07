from rest_framework.viewsets import ModelViewSet
from .models import CallMarkaz, QabulHujjati, AbiturientBakalavr, AbiturientMagistr
from .serialazer import CallMarkazSerializer, QabulHujjatiSerializer, AbiturientBakalavrSerializer, AbiturientMagistrSerializer


class CallMarkazViewSet(ModelViewSet):
    queryset = CallMarkaz.objects.all()
    serializer_class = CallMarkazSerializer

    

class QabulHujjatiViewSet(ModelViewSet):
    queryset = QabulHujjati.objects.all()
    serializer_class = QabulHujjatiSerializer


class AbiturientBakalavrViewSet(ModelViewSet):
    queryset = AbiturientBakalavr.objects.all()
    serializer_class = AbiturientBakalavrSerializer


class AbiturientMagistrViewSet(ModelViewSet):
    queryset = AbiturientMagistr.objects.all()
    serializer_class = AbiturientMagistrSerializer

