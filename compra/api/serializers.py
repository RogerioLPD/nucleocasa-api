from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from compra.models import Compra

Usuario = get_user_model()


class EmpresaCompraSerializer(ModelSerializer):
    class Meta:
        ref_name = "Empresa compra"
        model = Usuario
        fields = ['foto', 'first_name', 'last_name', 'email', 'tipo']


class EspecificadorSerializer(ModelSerializer):
    class Meta:
        ref_name = "Especificado"
        model = Usuario
        fields = ['foto', 'first_name', 'last_name', 'email', 'tipo']


class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = "__all__"


class CriarCompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = ['valor', 'especificador', 'empresa', ]


class ComprasEspeficadorSerializer(ModelSerializer):
    empresa = EmpresaCompraSerializer()

    class Meta:
        model = Compra
        fields = ['valor', 'empresa', ]
