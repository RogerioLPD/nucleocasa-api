from django.contrib.auth import get_user_model
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

Usuario = get_user_model()


class UsuarioSerializer(ModelSerializer):
    foto = Base64ImageField(required=False)

    class Meta:
        model = Usuario
        fields = '__all__'
        # fields = ['id', 'foto', 'nome', 'sobrenome', 'email', 'celular', 'cidade', 'latitude', 'longitude', ]


class ChangePasswordSerializer(serializers.Serializer):
    model = Usuario

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


'''
Serialzierss que gerenciam as Empresas
'''


class CriarEmpresaSerializer(ModelSerializer):
    foto = Base64ImageField(required=True)

    class Meta:
        model = Usuario
        fields = ['foto', 'email', 'password', 'nome', 'cidade', ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        usuario = Usuario(username=validated_data['email'], **validated_data)
        usuario.set_password(validated_data['password'])
        usuario.save()
        return usuario


class EmpresaSerializer(ModelSerializer):
    class Meta:
        ref_name = "Empresa Serializer"

    class Meta:
        model = Usuario
        fields = ['id', 'foto', 'email', 'nome', 'cnpj', 'tipo', 'seguimento', 'telefone', 'celular', 'endereco', 'numero',
                  'bairro', 'cidade', 'estado', ]


'''
Serialzierss que gerenciam as Especificadors
'''


class CriarEspecificadorSerializer(ModelSerializer):
    cpf = serializers.CharField(required=True)

    class Meta:
        model = Usuario
        fields = ['email', 'password', 'nome', 'cpf', 'tipo', 'seguimento', 'telefone', 'celular', 'endereco',
                  'numero',
                  'bairro', 'cidade', 'estado', ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        usuario = Usuario(username=validated_data['email'], **validated_data)
        usuario.set_password(validated_data['password'])
        usuario.save()
        return usuario


class EspecificadorSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'foto', 'email', 'nome', 'cpf', 'tipo', 'seguimento', 'telefone', 'celular', 'endereco',
                  'numero',
                  'bairro', 'cidade', 'estado', ]
