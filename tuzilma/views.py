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
    http_method_names = ['get', 'post', 'put', 'delete']

class RektoratRahbarViewSet(ModelViewSet):
    queryset = RektoratRahbar.objects.all()
    serializer_class = RektoratRahbarSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class RektoratHodimViewSet(ModelViewSet):
    queryset = RektoratHodim.objects.all()
    serializer_class = RektoratHodimSerializer
    http_method_names = ['get', 'post', 'put', 'delete']




class FakultetViewSet(ModelViewSet):
    queryset = Fakultet.objects.all()
    serializer_class = FakultetSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class FakultetRahbarViewSet(ModelViewSet):
    queryset = FakultetRahbar.objects.all()
    serializer_class = FakultetRahbarSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class FakultetHodimViewSet(ModelViewSet):
    queryset = FakultetHodim.objects.all()
    serializer_class = FakultetHodimSerializer
    http_method_names = ['get', 'post', 'put', 'delete']



    
class KafedraViewSet(ModelViewSet):
    queryset = Kafedra.objects.all()
    serializer_class = KafedraSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class KafedraRahbarViewSet(ModelViewSet):
    queryset = KafedraRahbar.objects.all()
    serializer_class = KafedraRahbarSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class KafedraHodimViewSet(ModelViewSet):
    queryset = KafedraHodim.objects.all()
    serializer_class = KafedraHodimSerializer
    http_method_names = ['get', 'post', 'put', 'delete']



    
class BolimViewSet(ModelViewSet):
    queryset = Bolim.objects.all()
    serializer_class = BolimSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class BolimRahbarViewSet(ModelViewSet):
    queryset = BolimRahbar.objects.all()
    serializer_class = BolimRahbarSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class BolimHodimViewSet(ModelViewSet):
    queryset = BolimHodim.objects.all()
    serializer_class = BolimHodimSerializer
    http_method_names = ['get', 'post', 'put', 'delete']



    
class MarkazViewSet(ModelViewSet):
    queryset = Markaz.objects.all()
    serializer_class = MarkazSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class MarkazRahbarViewSet(ModelViewSet):
    queryset = MarkazRahbar.objects.all()
    serializer_class = MarkazRahbarSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class MarkazHodimViewSet(ModelViewSet):
    queryset = MarkazHodim.objects.all()
    serializer_class = MarkazHodimSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

