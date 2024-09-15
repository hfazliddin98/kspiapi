from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import JamoatchilikViewSet, MadaniyViewSet, OquvViewSet, AkademikViewSet, IlmiyViewSet, YoshlarViewSet
from .views import  NormativHujatlarViewSet, IchkiIdoraviyHujatlarViewSet, XabarBerishViewSet



router = SimpleRouter()

router.register('jamoatchilik', JamoatchilikViewSet, basename='jamoatchilik')
router.register('madaniy', MadaniyViewSet, basename='madaniy')
router.register('oquv', OquvViewSet, basename='oquv')
router.register('akademik', AkademikViewSet, basename='akademik')
router.register('ilmiy', IlmiyViewSet, basename='ilmiy')
router.register('yoshlar', YoshlarViewSet, basename='yoshlar')
router.register('normativ_hujatlar', NormativHujatlarViewSet, basename='normativ_hujatlar')
router.register('ichki_idoraviy_hujatlar', IchkiIdoraviyHujatlarViewSet, basename='ichki_idoraviy_hujatlar')
router.register('xabar_berish', XabarBerishViewSet, basename='xabar_berish')



urlpatterns = []
urlpatterns += router.urls


