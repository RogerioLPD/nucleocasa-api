from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import *

from compra.api.serializers import CompraSerializer, CriarCompraSerializer, ComprasEspeficadorSerializer
from compra.models import Compra


class CompraViewSet(GenericViewSet, ListAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    permission_classes = [IsAuthenticated, ]


class CriarCompraViewSet(GenericViewSet, CreateModelMixin):
    queryset = Compra.objects.all()
    serializer_class = CriarCompraSerializer
    permission_classes = [IsAuthenticated, ]


class ComprasEspecificadorViewSet(GenericViewSet, ListAPIView):
    queryset = Compra.objects.all()
    serializer_class = ComprasEspeficadorSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return self.queryset.filter(especificador=self.request.user)
