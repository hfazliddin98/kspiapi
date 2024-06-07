from rest_framework.routers import SimpleRouter
from .views import TalabaBakalavrViewSet, TalabaMagistrViewSet
from .views import BakalavrMalakaTalabiViewSet, BakalavrOquvRejaTuriViewSet, BakalavrOquvRejaViewSet
from .views import BakalavrFanDasturTuriViewSet, BakalavrFanDasturViewSet, BakalavrFanKatalogiViewSet


router = SimpleRouter()

router.register('bakalavr', TalabaBakalavrViewSet, basename='bakalavr')
router.register('magistr', TalabaMagistrViewSet, basename='magistr')
router.register('malaka_talab', BakalavrMalakaTalabiViewSet, basename='malaka_talab')
router.register('oquv_reja_tur', BakalavrOquvRejaTuriViewSet, basename='oquv_reja_tur')
router.register('oquv_reja', BakalavrOquvRejaViewSet, basename='oquv_reja')



urlpatterns = []
urlpatterns += router.urls