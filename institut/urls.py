from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import InstitutHaqidaViewSet, InstitutMalumotlariViewSet, KengashViewSet, TuzilmaViewSet, InstitutRekvizitiViewSet, BankRekvizitiViewSet, QabulxonaViewSet


router = SimpleRouter()

router.register('instituthaqida', InstitutHaqidaViewSet, basename='instituthaqida')
router.register('institutmalumotlari', InstitutMalumotlariViewSet, basename='institutmalumotlari')
router.register('kengash', KengashViewSet, basename='kengash')
router.register('tuzilma', TuzilmaViewSet, basename='tuzilma')
router.register('institutrekviziti', InstitutRekvizitiViewSet, basename='institutrekviziti')
router.register('bankrekviziti', BankRekvizitiViewSet, basename='bankrekviziti')
router.register('qabulxona', QabulxonaViewSet, basename='qabulxona')


urlpatterns = []
urlpatterns += router.urls