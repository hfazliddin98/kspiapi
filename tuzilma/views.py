from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Rektorat, Fakultet, Kafedra, Bolim, Markaz
from .models import RektoratRahbar, FakultetRahbar, KafedraRahbar, BolimRahbar, MarkazRahbar
from .models import RektoratHodim, FakultetHodim, KafedraHodim, BolimHodim, MarkazHodim
from .serialazer import RektoratSerializer, FakultetSerializer, KafedraSerializer, BolimSerializer, MarkazSerializer
from .serialazer import RektoratRahbarSerializer, FakultetRahbarSerializer, KafedraRahbarSerializer, BolimRahbarSerializer, MarkazRahbarSerializer
from .serialazer import RektoratHodimSerializer, FakultetHodimSerializer, KafedraHodimSerializer, BolimHodimSerializer, MarkazHodimSerializer


class RektoratViewSet(ModelViewSet):
    queryset = Rektorat.objects.all()
    serializer_class = RektoratSerializer


class RektoratRahbarViewSet(ModelViewSet):
    queryset = RektoratRahbar.objects.all()
    serializer_class = RektoratRahbarSerializer


class RektoratHodimViewSet(ModelViewSet):
    queryset = RektoratHodim.objects.all()
    serializer_class = RektoratHodimSerializer


class FakultetViewSet(ModelViewSet):
    queryset = Fakultet.objects.all()
    serializer_class = FakultetSerializer


class FakultetRahbarViewSet(ModelViewSet):
    queryset = FakultetRahbar.objects.all()
    serializer_class = FakultetRahbarSerializer


class FakultetHodimViewSet(ModelViewSet):
    queryset = FakultetHodim.objects.all()
    serializer_class = FakultetHodimSerializer


class KafedraViewSet(ModelViewSet):
    queryset = Kafedra.objects.all()
    serializer_class = KafedraSerializer


class KafedraRahbarViewSet(ModelViewSet):
    queryset = KafedraRahbar.objects.all()
    serializer_class = KafedraRahbarSerializer


class KafedraHodimViewSet(ModelViewSet):
    queryset = KafedraHodim.objects.all()
    serializer_class = KafedraHodimSerializer


class BolimViewSet(ModelViewSet):
    queryset = Bolim.objects.all()
    serializer_class = BolimSerializer


class BolimRahbarViewSet(ModelViewSet):
    queryset = BolimRahbar.objects.all()
    serializer_class = BolimRahbarSerializer


class BolimHodimViewSet(ModelViewSet):
    queryset = BolimHodim.objects.all()
    serializer_class = BolimHodimSerializer


class MarkazViewSet(ModelViewSet):
    queryset = Markaz.objects.all()
    serializer_class = MarkazSerializer


class MarkazRahbarViewSet(ModelViewSet):
    queryset = MarkazRahbar.objects.all()
    serializer_class = MarkazRahbarSerializer


class MarkazHodimViewSet(ModelViewSet):
    queryset = MarkazHodim.objects.all()
    serializer_class = MarkazHodimSerializer


