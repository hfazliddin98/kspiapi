from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import InstitutHaqidaViewSet, InstitutMalumotlariViewSet, KengashViewSet, TuzilmaViewSet, InstitutRekvizitiViewSet, BankRekvizitiViewSet, QabulxonaViewSet
from .views import KorupsiyagaXabarViewSet, PrizdentFarmonlariViewSet, QonunlarViewSet, VazirlarMahkamasiQarorlariViewSet
from .views import IchkiMeyoriyHujatlarViewSet


router = SimpleRouter()

router.register('institut_haqida', InstitutHaqidaViewSet, basename='institut_haqida')
router.register('institut_malumotlari', InstitutMalumotlariViewSet, basename='institut_malumotlari')
router.register('kengash', KengashViewSet, basename='kengash')
router.register('tuzilma', TuzilmaViewSet, basename='tuzilma')
router.register('institut_rekviziti', InstitutRekvizitiViewSet, basename='institut_rekviziti')
router.register('bank_rekviziti', BankRekvizitiViewSet, basename='bank_rekviziti')
router.register('qabulxona', QabulxonaViewSet, basename='qabulxona')
router.register('korupsiyagaxabar', KorupsiyagaXabarViewSet, basename='korupsiyagaxabar')
router.register('prizdent_farmonlari', PrizdentFarmonlariViewSet, basename='prizdent_farmonlari')
router.register('qonunlar', QonunlarViewSet, basename='qonunlar')
router.register('vazirlar_mahkamasi_qarorlari', VazirlarMahkamasiQarorlariViewSet, basename='vazirlar_mahkamasi_qarorlari')
router.register('ichki_meyoriy_hujatlar', IchkiMeyoriyHujatlarViewSet, basename='ichki_meyoriy_hujatlar')


urlpatterns = []
urlpatterns += router.urls