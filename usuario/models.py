from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail


class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        usuario = self.model(email=email, username=email, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Staff precisa ter is_staff=True')
        return self._create_user(email, password, **extra_fields)


class Usuario(AbstractUser):
    TIPO_CHOICES = [
        ('EMPRESA', 'Empresa'),
        ('ESPECIFICADOR', 'Especificador'),
    ]
    foto = models.ImageField(upload_to='usuario', blank=True, null=True)
    email = models.EmailField('E-mail', unique=True)
    nome = models.CharField('Nome', max_length=100)
    seguimento = models.CharField('Seguimento', max_length=40)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='EMPRESA')
    cnpj = models.CharField('CNPJ', max_length=20, unique=True, blank=True, null=True)
    cpf = models.CharField('CPF', max_length=20, unique=True, blank=True, null=True)
    telefone = models.CharField('Telefone', max_length=20, blank=True, null=True)
    celular = models.CharField('Celular', max_length=20, blank=True, null=True)
    endereco = models.CharField('Endereço', max_length=20, blank=True, null=True)
    numero = models.CharField('Número', max_length=10, blank=True, null=True)
    bairro = models.CharField('Bairro', max_length=30, blank=True, null=True)
    cidade = models.CharField('Cidade', max_length=30)
    estado = models.CharField('Estado', max_length=30, blank=True, null=True)
    cep = models.CharField('CEP', max_length=12, blank=True, null=True)
    is_staff = models.BooleanField('Membro da Equipe', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', ]

    def __str__(self):
        return self.email

    objects = UsuarioManager()


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )