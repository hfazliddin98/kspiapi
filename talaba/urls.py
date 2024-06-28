from rest_framework.routers import SimpleRouter
from .views import TalabaBakalavrViewSet, TalabaMagistrViewSet
from .views import BakalavrMalakaTalabiViewSet, BakalavrOquvRejaTuriViewSet, BakalavrOquvRejaViewSet
from .views import BakalavrFanDasturTuriViewSet, BakalavrFanDasturViewSet, BakalavrFanKatalogiViewSet
from .views import TTJArizaViewSet, TTJCampusViewSet, TTJRahbarViewSet, TTJStatistikaViewSet


router = SimpleRouter()

router.register('bakalavr', TalabaBakalavrViewSet, basename='bakalavr')
router.register('magistr', TalabaMagistrViewSet, basename='magistr')
router.register('malaka_talab', BakalavrMalakaTalabiViewSet, basename='malaka_talab')
router.register('oquv_reja_tur', BakalavrOquvRejaTuriViewSet, basename='oquv_reja_tur')
router.register('oquv_reja', BakalavrOquvRejaViewSet, basename='oquv_reja')

router.register('ttj_ariza', TTJArizaViewSet, basename='ttj_ariza')
router.register('ttj_campus', TTJCampusViewSet, basename='ttj_campus')
router.register('ttj_rahbar', TTJRahbarViewSet, basename='ttj_rahbar')
router.register('ttj_statistika', TTJStatistikaViewSet, basename='ttj_statistika')



urlpatterns = []
urlpatterns += router.urls