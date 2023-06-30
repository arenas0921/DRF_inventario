from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    precio = models.IntegerField
    activo = models.BooleanField(default=True)
    x = models.BooleanField(default=True)