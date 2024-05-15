from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import YangilikViewSet, ElonViewSet, GalareyaTuriViewSet, GalareyaViewSet, FikrViewSet, VideoMaruzalarViewSet, MasofaviyTalimViewSet
from .views import TalabaViewSet, HamkorlarimizViewSet, StatistikaViewSet, ElektronKutubxonaViewSet, VirtualQabulxonaViewSet, FakultetViewSet


router = SimpleRouter()

router.register('yangilik', YangilikViewSet, basename='yangilik')
router.register('elon', ElonViewSet, basename='elon')
router.register('galareya/tur', GalareyaTuriViewSet, basename='galareya/tur')
router.register('galareya', GalareyaViewSet, basename='galareya')
router.register('fikr', FikrViewSet, basename='fikr')
router.register('talaba/', TalabaViewSet, basename='talaba/')
router.register('hamkorlarimiz', HamkorlarimizViewSet, basename='hamkorlarimiz')
router.register('statistika', StatistikaViewSet, basename='statistika')
router.register('elektronkutubxona', ElektronKutubxonaViewSet, basename='elektronkutubxona')
router.register('videomaruzalar', VideoMaruzalarViewSet, basename='videomaruzalar')
router.register('virtualqabulxona', VirtualQabulxonaViewSet, basename='virtualqabulxona')
router.register('masofaviytalim', MasofaviyTalimViewSet, basename='masofaviytalim')
router.register('fakultet', FakultetViewSet, basename='fakultet')


urlpatterns = []
urlpatterns += router.urls


