from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import *

from empresa.api.serializers import EmpresasSerializer

Usuario = get_user_model()


class EmpresasViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = EmpresasSerializer

    def get_queryset(self):
        return self.queryset.filter(tipo='EMPRESA')
