from django.db import models

from django.db import models
class Estoque(models.Model):
    produto = models.CharField(max_length=100, null= False, blank=False)
    data_compra = models.DateField(null=False, blank=False)
    data_vencimento = models.DateField(null=False, blank=False)
    quantidade = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)