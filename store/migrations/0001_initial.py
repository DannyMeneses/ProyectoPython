# Generated by Django 4.2.5 on 2023-09-05 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('image', models.ImageField(upload_to='promoción', verbose_name='Imagen')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateField(auto_now=True, verbose_name='Fecha de modificación')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['-created'],
            },
        ),
    ]