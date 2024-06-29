from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import CallMarkazViewSet, QabulHujjatiViewSet, AbiturientBakalavrViewSet, AbiturientMagistrViewSet
from .views import BaxoMezoniViewSet, KvotaViewSet


router = SimpleRouter()

router.register('callmarkaz', CallMarkazViewSet, basename='callmarkaz')
router.register('qabulhujatlari', QabulHujjatiViewSet, basename='qabulhujatlari')
router.register('bakalavr', AbiturientBakalavrViewSet, basename='bakalavr')
router.register('magistr', AbiturientMagistrViewSet, basename='magistr')
router.register('baxo_mezoni', BaxoMezoniViewSet, basename='baxo_mezoni')
router.register('kvota', KvotaViewSet, basename='kvota')

urlpatterns = []
urlpatterns += router.urls


