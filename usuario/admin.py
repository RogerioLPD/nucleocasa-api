from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UsuarioChangeForm, UsuarioCreationForm
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    add_form = UsuarioCreationForm
    form = UsuarioChangeForm
    model = Usuario
    list_display = ('email', 'nome', 'cnpj', 'cpf', 'is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('foto',
                                             'nome', 'cnpj', 'tipo', 'seguimento', 'cpf', 'telefone', 'celular',
                                             'endereco', 'numero', 'bairro', 'cep',
                                             'cidade', 'estado',)}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )
