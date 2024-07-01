from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import YangilikViewSet, ElonViewSet, GalareyaTuriViewSet, GalareyaViewSet, FikrViewSet, VideoMaruzalarViewSet, MasofaviyTalimViewSet
from .views import TalabaViewSet, HamkorlarimizViewSet, StatistikaViewSet, ElektronKutubxonaViewSet, VirtualQabulxonaViewSet
from .views import BoglanishViewSet, VakansiyaViewSet, EfirNameViewSet, EfirViewSet



router = SimpleRouter()

router.register('yangilik', YangilikViewSet, basename='yangilik')
router.register('elon', ElonViewSet, basename='elon')
router.register('galareya_tur', GalareyaTuriViewSet, basename='galareya_tur')
router.register('galareya', GalareyaViewSet, basename='galareya')
router.register('fikr', FikrViewSet, basename='fikr')
router.register('talaba', TalabaViewSet, basename='talaba')
router.register('hamkorlarimiz', HamkorlarimizViewSet, basename='hamkorlarimiz')
router.register('statistika', StatistikaViewSet, basename='statistika')
router.register('elektronkutubxona', ElektronKutubxonaViewSet, basename='elektronkutubxona')
router.register('videomaruzalar', VideoMaruzalarViewSet, basename='videomaruzalar')
router.register('virtualqabulxona', VirtualQabulxonaViewSet, basename='virtualqabulxona')
router.register('masofaviytalim', MasofaviyTalimViewSet, basename='masofaviytalim')
router.register('boglanish', BoglanishViewSet, basename='boglanish')
router.register('vakansiya', VakansiyaViewSet, basename='vakansiya')
router.register('efir_name', EfirNameViewSet, basename='efir_name')
router.register('efir', EfirViewSet, basename='efir')



urlpatterns = []
urlpatterns += router.urls


