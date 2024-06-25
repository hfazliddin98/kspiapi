from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import JamoatchilikViewSet, MadaniyViewSet, OquvViewSet, AkademikViewSet, IlmiyViewSet, YoshlarViewSet




router = SimpleRouter()

router.register('jamoatchilik', JamoatchilikViewSet, basename='jamoatchilik')
router.register('madaniy', MadaniyViewSet, basename='madaniy')
router.register('oquv', OquvViewSet, basename='oquv')
router.register('akademik', AkademikViewSet, basename='akademik')
router.register('ilmiy', IlmiyViewSet, basename='ilmiy')
router.register('yoshlar', YoshlarViewSet, basename='yoshlar')



urlpatterns = []
urlpatterns += router.urls


