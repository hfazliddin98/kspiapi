from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import AllowAny # type: ignore
from .models import Yangilik, Elon, GalareyaTuri, Galareya, Fikr, Talaba, Hamkorlarimiz, Statistika, ElektronKutubxona, MasofaviyTalim, VirtualQabulxona, VideoMaruzalar, Fakultet
from .models import NavbarName, NavbarLink
from .serialazer import YangilikSerializer, ElonSerializer, GalareyaTuriSerializer, GalareyaSerializer, FikrSerializer, HamkorlarimizSerializer, TalabaSerializer
from .serialazer import ElektronKutubxonaSerializer, VirtualQabulxonaSerializer, VideoMaruzalarSerializer, MasofaviyTalimSerializer, StatistikaSerializer, FakultetSerializer
from .serialazer import NavbarNameSerializer, NavbarLinkSerializer



class YangilikViewSet(ModelViewSet):
    queryset = Yangilik.objects.all()
    serializer_class = YangilikSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    

class ElonViewSet(ModelViewSet):
    queryset = Elon.objects.all()
    serializer_class = ElonSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    

class GalareyaTuriViewSet(ModelViewSet):
    queryset = GalareyaTuri.objects.all()
    serializer_class = GalareyaTuriSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    

class GalareyaViewSet(ModelViewSet):
    queryset = Galareya.objects.all()
    serializer_class = GalareyaSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    

class FikrViewSet(ModelViewSet):
    queryset = Fikr.objects.all()
    serializer_class = FikrSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    

class HamkorlarimizViewSet(ModelViewSet):
    queryset = Hamkorlarimiz.objects.all()
    serializer_class = HamkorlarimizSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    

class StatistikaViewSet(ModelViewSet):
    queryset = Statistika.objects.all()
    serializer_class = StatistikaSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    

class TalabaViewSet(ModelViewSet):
    queryset = Talaba.objects.all()
    serializer_class = TalabaSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    

class ElektronKutubxonaViewSet(ModelViewSet):
    queryset = ElektronKutubxona.objects.all()
    serializer_class = ElektronKutubxonaSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    

class MasofaviyTalimViewSet(ModelViewSet):
    queryset = MasofaviyTalim.objects.all()
    serializer_class = MasofaviyTalimSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    

class VideoMaruzalarViewSet(ModelViewSet):
    queryset = VideoMaruzalar.objects.all()
    serializer_class = VideoMaruzalarSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    

class VirtualQabulxonaViewSet(ModelViewSet):
    queryset = VirtualQabulxona.objects.all()
    serializer_class = VirtualQabulxonaSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    

class FakultetViewSet(ModelViewSet):
    queryset = Fakultet.objects.all()
    serializer_class = FakultetSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    
class NavbarNameViewSet(ModelViewSet):
    queryset = NavbarName.objects.all()
    serializer_class = NavbarNameSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    
class NavbarLinkViewSet(ModelViewSet):
    queryset = NavbarLink.objects.all()
    serializer_class = NavbarLinkSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    