from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50, verbose_name='Nombre')
    created=models.DateField(auto_now_add=True, verbose_name='Fecha de creación')
    updated=models.DateField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
        ordering=['name']
    def __str__(self):
        return self.name

class Trayectoria(models.Model):
    title=models.CharField(max_length=100, verbose_name='Titulo')
    Content=models.TextField(verbose_name='Contenido')
    image=models.ImageField(verbose_name='Imagen', upload_to='trayectoria')
    published=models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    author=models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    categories=models.ManyToManyField(Category, verbose_name='Categorias')
    created=models.DateField(auto_now_add=True, verbose_name='Fecha de creación')
    updated=models.DateField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name='Entrada'
        verbose_name_plural='Entradas'
        ordering=['-created']
    def __str__(self):
        return self.title