from rest_framework.viewsets import ModelViewSet
from .models import CallMarkaz, QabulHujjati, AbiturientBakalavr, AbiturientMagistr
from .models import BaxoMezoni, Kvota
from .serialazer import BaxoMezoniSerializer, KvotaSerializer
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


class BaxoMezoniViewSet(ModelViewSet):
    queryset = BaxoMezoni.objects.all()
    serializer_class = BaxoMezoniSerializer


class KvotaViewSet(ModelViewSet):
    queryset = Kvota.objects.all()
    serializer_class = KvotaSerializer
