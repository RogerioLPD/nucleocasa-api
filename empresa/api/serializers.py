from django.contrib.auth import get_user_model
from drf_extra_fields.fields import Base64ImageField
from rest_framework.serializers import ModelSerializer

Usuario = get_user_model()


class EmpresasSerializer(ModelSerializer):

    foto = Base64ImageField()

    class Meta:
        model = Usuario
        fields = ['foto', 'nome', 'cidade', ]
