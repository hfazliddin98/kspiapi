from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import InstitutHaqidaViewSet, InstitutMalumotlariViewSet, KengashViewSet, TuzilmaViewSet, InstitutRekvizitiViewSet, BankRekvizitiViewSet, QabulxonaViewSet
from .views import KorupsiyagaXabarViewSet


router = SimpleRouter()

router.register('institut_haqida', InstitutHaqidaViewSet, basename='institut_haqida')
router.register('institut_malumotlari', InstitutMalumotlariViewSet, basename='institut_malumotlari')
router.register('kengash', KengashViewSet, basename='kengash')
router.register('tuzilma', TuzilmaViewSet, basename='tuzilma')
router.register('institut_rekviziti', InstitutRekvizitiViewSet, basename='institut_rekviziti')
router.register('bank_rekviziti', BankRekvizitiViewSet, basename='bank_rekviziti')
router.register('qabulxona', QabulxonaViewSet, basename='qabulxona')
router.register('korupsiyagaxabar', KorupsiyagaXabarViewSet, basename='korupsiyagaxabar')


urlpatterns = []
urlpatterns += router.urls