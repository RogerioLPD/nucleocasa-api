from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario


class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('nome', )
        labels = {'username': 'e-mail'}

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data['password1'])
        usuario.email = self.cleaned_data['username']
        if commit:
            usuario.save()
        return usuario


class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ('nome', )
        labels = {'username': 'e-mail'}


class UserAdminCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'username', ]
        labels = {'username': 'e-mail'}

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.email = self.cleaned_data['username']
        if commit:
            usuario.save()
        return usuario
