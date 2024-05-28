from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import CallMarkazViewSet


router = SimpleRouter()

router.register('callmarkaz', CallMarkazViewSet, basename='callmarkaz')


urlpatterns = []
urlpatterns += router.urls


