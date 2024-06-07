from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import CallMarkazViewSet, QabulHujjatiViewSet, AbiturientBakalavrViewSet, AbiturientMagistrViewSet


router = SimpleRouter()

router.register('callmarkaz', CallMarkazViewSet, basename='callmarkaz')
router.register('qabulhujatlari', QabulHujjatiViewSet, basename='qabulhujatlari')
router.register('bakalavr', AbiturientBakalavrViewSet, basename='bakalavr')
router.register('magistr', AbiturientMagistrViewSet, basename='magistr')


urlpatterns = []
urlpatterns += router.urls


