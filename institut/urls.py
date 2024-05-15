from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import InstitutHaqidaViewSet


router = SimpleRouter()

router.register('instituthaqida', InstitutHaqidaViewSet, basename='instituthaqida')


urlpatterns = []
urlpatterns += router.urls