from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import CallMarkazViewSet, QabulHujjatiViewSet, BakalavrViewSet, ModelViewSet


router = SimpleRouter()

router.register('callmarkaz', CallMarkazViewSet, basename='callmarkaz')
router.register('qabulhujatlari', QabulHujjatiViewSet, basename='qabulhujatlari')
router.register('bakalavr', BakalavrViewSet, basename='bakalavr')
router.register('magistr', ModelViewSet, basename='magistr')


urlpatterns = []
urlpatterns += router.urls


