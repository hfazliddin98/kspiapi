from rest_framework.routers import SimpleRouter


router = SimpleRouter()

# router.register('rektorat', RektoratViewSet, basename='rektorat')



urlpatterns = []
urlpatterns += router.urls