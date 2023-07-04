from django.contrib.auth import get_user_model
from django.db import models


class Compra(models.Model):
    empresa = models.ForeignKey(get_user_model(), related_name="compra_empresa", on_delete=models.CASCADE)
    especificador = models.ForeignKey(get_user_model(), related_name="compra_especificador", on_delete=models.CASCADE)
    valor = models.CharField(max_length=10)
    criado_em: models.DateTimeField(auto_now_add=True)
    atualizado_em: models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

    def __str__(self):
        return '%s - %s' % (self.empresa, self.especificador)
