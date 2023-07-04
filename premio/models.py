from django.db import models


class Premio(models.Model):
    imagem_1 = models.ImageField(upload_to='premios')
    imagem_2 = models.ImageField(upload_to='premios', blank=True, null=True)
    imagem_3 = models.ImageField(upload_to='premios', blank=True, null=True)
    imagem_4 = models.ImageField(upload_to='premios', blank=True, null=True)
    imagem_5 = models.ImageField(upload_to='premios', blank=True, null=True)
    imagem_6 = models.ImageField(upload_to='premios', blank=True, null=True)
    pontos = models.IntegerField()
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=1000)
    criado_em: models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
