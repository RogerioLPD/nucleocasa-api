from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import *

from compra.api.serializers import CompraSerializer, CriarCompraSerializer, ComprasEspeficadorSerializer
from compra.models import Compra

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q

Usuario = get_user_model()


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


class NovaCompraView(APIView):
    def post(self, request):
        doc = self.request.data.dict()['doc']
        valor = self.request.data.dict()['valor']

        try:
            # Buscar o usuário pelo CPF ou CNPJ
            especificador = Usuario.objects.get(Q(cpf=doc) | Q(cnpj=doc))
        except Usuario.DoesNotExist:
            return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        nova_compra = Compra(valor=str(valor), especificador=especificador, empresa=self.request.user)

        nova_compra.save()

        serializer = CompraSerializer(nova_compra)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
