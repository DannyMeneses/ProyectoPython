from django.db import models

# Create your models here.
class Store(models.Model):
    title=models.CharField(max_length=100, verbose_name='Titulo')
    description=models.TextField(verbose_name='Descripción')
    image=models.ImageField(verbose_name='Imagen', upload_to='promoción')
    created=models.DateField(auto_now_add=True, verbose_name='Fecha de creación')
    updated=models.DateField(auto_now=True, verbose_name='Fecha de modificación')
    class Meta:
        verbose_name='Oferta'
        verbose_name_plural='Ofertas'
        ordering=['-created']
    def __str__(self):
        return self.title