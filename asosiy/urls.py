from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users.views import home



schema_view = get_schema_view(
   openapi.Info(
      title="Kengash uchun API",
      default_version='v1',
      description="Kengash uchun yaratilgan API",
      terms_of_service="https://kspi.uz",
      contact=openapi.Contact(email="hatamovfazliddin5@gmail.com"),
      license=openapi.License(name="Kengash License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('haker/', admin.site.urls),
    path('', home, name='home'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('yangilik/', include('yangilik.urls')),
    # path('api/v1/taklif/', include('taklif.urls')),
    # path('api/v1/statistika/', include('statistika.urls')),
    # path('api/v1/users/', include('users.urls')),
    # path('api/v1/davomat/', include('davomat.urls')),

    # registiratsiya
   #  path('api-auth/', include('rest_framework.urls')),
   #  path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),

    # swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)