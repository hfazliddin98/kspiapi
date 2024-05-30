from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import RektoratViewSet, RektoratRahbarViewSet, RektoratHodimViewSet
from .views import FakultetViewSet, FakultetRahbarViewSet, FakultetHodimViewSet
from .views import KafedraViewSet, KafedraRahbarViewSet, KafedraHodimViewSet
from .views import BolimViewSet, BolimRahbarViewSet, BolimHodimViewSet
from .views import MarkazViewSet, MarkazRahbarViewSet, MarkazHodimViewSet


router = SimpleRouter()

router.register('rektorat', RektoratViewSet, basename='rektorat')
router.register('rektorat/rahbar', RektoratRahbarViewSet, basename='rektorat/rahbar')
router.register('rektorat/hodim', RektoratHodimViewSet, basename='rektorat/hodim')

router.register('fakultet', FakultetViewSet, basename='fakultet')
router.register('fakultet/rahbar', FakultetRahbarViewSet, basename='fakultet/rahbar')
router.register('fakultet/hodim', FakultetHodimViewSet, basename='fakultet/hodim')

router.register(' kafedra',  KafedraViewSet, basename=' kafedra')
router.register(' kafedra/rahbar',  KafedraRahbarViewSet, basename=' kafedra/rahbar')
router.register(' kafedra/hodim',  KafedraHodimViewSet, basename=' kafedra/hodim')

router.register('bolim', BolimViewSet, basename='bolim')
router.register('bolim/rahbar', BolimRahbarViewSet, basename='bolim/rahbar')
router.register('bolim/hodim', BolimHodimViewSet, basename='bolim/hodim')

router.register('markaz', MarkazViewSet, basename='markaz')
router.register('markaz/rahbar', MarkazRahbarViewSet, basename='markaz/rahbar')
router.register('markaz/hodim', MarkazHodimViewSet, basename='markaz/hodim')


urlpatterns = []
urlpatterns += router.urls