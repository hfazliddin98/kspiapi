from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import RektoratViewSet, RektoratRahbarViewSet, RektoratHodimViewSet
from .views import FakultetViewSet, FakultetRahbarViewSet, FakultetHodimViewSet
from .views import KafedraViewSet, KafedraRahbarViewSet, KafedraHodimViewSet
from .views import BolimViewSet, BolimRahbarViewSet, BolimHodimViewSet
from .views import MarkazViewSet, MarkazRahbarViewSet, MarkazHodimViewSet


router = SimpleRouter()

router.register('rektorat', RektoratViewSet, basename='rektorat')
router.register('rektorat_rahbar', RektoratRahbarViewSet, basename='rektorat_rahbar')
router.register('rektorat_hodim', RektoratHodimViewSet, basename='rektorat_hodim')

router.register('fakultet', FakultetViewSet, basename='fakultet')
router.register('fakultet_rahbar', FakultetRahbarViewSet, basename='fakultet_rahbar')
router.register('fakultet_hodim', FakultetHodimViewSet, basename='fakultet_hodim')

router.register('kafedra',  KafedraViewSet, basename='kafedra')
router.register('kafedra_rahbar',  KafedraRahbarViewSet, basename='kafedra_rahbar')
router.register('kafedra_hodim',  KafedraHodimViewSet, basename='kafedra_hodim')

router.register('bolim', BolimViewSet, basename='bolim')
router.register('bolim_rahbar', BolimRahbarViewSet, basename='bolim_rahbar')
router.register('bolim_hodim', BolimHodimViewSet, basename='bolim_hodim')

router.register('markaz', MarkazViewSet, basename='markaz')
router.register('markaz_rahbar', MarkazRahbarViewSet, basename='markaz_rahbar')
router.register('markaz_hodim', MarkazHodimViewSet, basename='markaz_hodim')


urlpatterns = []
urlpatterns += router.urls