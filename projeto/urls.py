from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from compra.api.viewsets import CompraViewSet, CriarCompraViewSet, ComprasEspecificadorViewSet
from empresa.api.viewsets import EmpresasViewSet
from premio.api.viewsets import PremioViewSet
from usuario.api.viewsets import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register(r'usuario', UsuarioViewSet)
router.register(r'cadastro/empresa', CriarEmpresaViewSet)
router.register(r'empresa', EmpresaViewSet)
router.register(r'empresas', EmpresasViewSet)
router.register(r'cadastro/especificador', CriarEspecificadorViewSet)
router.register(r'especificador', EspecificadorViewSet)
router.register(r'premio', PremioViewSet)
router.register(r'compra', CompraViewSet)
router.register(r'compra/nova', CriarCompraViewSet)
router.register(r'compras/especificador', ComprasEspecificadorViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('login/', obtain_auth_token),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('password-reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]

# swagger
urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # noqa E501
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
