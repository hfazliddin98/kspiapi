from rest_framework.routers import SimpleRouter
from .views import TalabaBakalavrViewSet, TalabaMagistrViewSet
from .views import BakalavrMalakaTalabiViewSet, BakalavrOquvRejaTuriViewSet, BakalavrOquvRejaViewSet
from .views import BakalavrFanDasturTuriViewSet, BakalavrFanDasturViewSet, BakalavrFanKatalogiViewSet
from .views import BakalavrFanDasturKursViewSet, BakalavrFanDasturYonalishViewSet
from .views import MagistrMalakaTalabiViewSet, MagistrOquvRejaTuriViewSet, MagistrOquvRejaViewSet
from .views import MagistrFanDasturTuriViewSet, MagistrFanDasturViewSet, MagistrFanKatalogiViewSet
from .views import MagistrFanDasturKursViewSet, MagistrFanDasturYonalishViewSet
from .views import TTJArizaViewSet, TTJCampusViewSet, TTJRahbarViewSet, TTJStatistikaViewSet


router = SimpleRouter()

router.register('bakalavr', TalabaBakalavrViewSet, basename='bakalavr')
router.register('magistr', TalabaMagistrViewSet, basename='magistr')

router.register('bakalavr_malaka_talab', BakalavrMalakaTalabiViewSet, basename='bakalavr_malaka_talab')
router.register('bakalavr_oquv_reja_tur', BakalavrOquvRejaTuriViewSet, basename='bakalavr_oquv_reja_tur')
router.register('bakalavr_oquv_reja', BakalavrOquvRejaViewSet, basename='bakalavr_oquv_reja')
router.register('bakalavr_fan_dastur_kurs', BakalavrFanDasturKursViewSet, basename='bakalavr_fan_dastur_kurs')
router.register('bakalavr_fan_dastur_yonalish', BakalavrFanDasturYonalishViewSet, basename='bakalavr_fan_dastur_yonalish')
router.register('bakalavr_fan_dastur_tur', BakalavrFanDasturTuriViewSet, basename='bakalavr_fan_dastur_tur')
router.register('bakalavr_fan_dastur', BakalavrFanDasturViewSet, basename='bakalavr_fan_dastur')
router.register('bakalavr_fan_katalog', BakalavrFanKatalogiViewSet, basename='bakalavr_fan_katalog')

router.register('magistr_malaka_talab', MagistrMalakaTalabiViewSet, basename='magistr_malaka_talab')
router.register('magistr_oquv_reja_tur', MagistrOquvRejaTuriViewSet, basename='magistr_oquv_reja_tur')
router.register('magistr_oquv_reja', MagistrOquvRejaViewSet, basename='magistr_oquv_reja')
router.register('magistr_fan_dastur_kurs', MagistrFanDasturKursViewSet, basename='magistr_fan_dastur_kurs')
router.register('magistr_fan_dastur_yonalish', MagistrFanDasturYonalishViewSet, basename='magistr_fan_dastur_yonalish')
router.register('magistr_fan_dastur_tur', MagistrFanDasturTuriViewSet, basename='magistr_fan_dastur_tur')
router.register('magistr_fan_dastur', MagistrFanDasturViewSet, basename='magistr_fan_dastur')
router.register('magistr_fan_katalog', MagistrFanKatalogiViewSet, basename='magistr_fan_katalog')

router.register('ttj_ariza', TTJArizaViewSet, basename='ttj_ariza')
router.register('ttj_campus', TTJCampusViewSet, basename='ttj_campus')
router.register('ttj_rahbar', TTJRahbarViewSet, basename='ttj_rahbar')
router.register('ttj_statistika', TTJStatistikaViewSet, basename='ttj_statistika')



urlpatterns = []
urlpatterns += router.urls