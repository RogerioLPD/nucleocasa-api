from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import *
from rest_framework.mixins import *

from usuario.api.serializers import *

Usuario = get_user_model()


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        return self.queryset.get(email=self.request.user.email)


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = Usuario
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
ViewSets que gerenciam as Empresas
'''


# Cria um novo usuário do tipo Empresa
class CriarEmpresaViewSet(GenericViewSet, CreateModelMixin):
    queryset = Usuario.objects.all()
    serializer_class = CriarEmpresaSerializer
    permission_classes = [IsAdminUser]


# Lista todos os usuários do tipo Empresa
class EmpresaViewSet(GenericViewSet, ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return self.queryset.filter(tipo="EMPRESA")


'''
ViewSets que gerenciam os Espectadores
'''


class CriarEspecificadorViewSet(GenericViewSet, CreateModelMixin):
    queryset = Usuario.objects.all()
    serializer_class = CriarEspecificadorSerializer


class EspecificadorViewSet(GenericViewSet, ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = EspecificadorSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return self.queryset.filter(tipo="ESPECIFICADOR")
