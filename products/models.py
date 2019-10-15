from django.db import models

# Create your models here.
class Client(models.Model):
    document    = models.IntegerField(verbose_name="Documento")
    first_name  = models.CharField(max_length=150, verbose_name="Nombres")
    last_name   = models.CharField(max_length=150, verbose_name="Apellidos")

    def __str__(self):
        return '%s: %s %s' % (self.document, self.first_name, self.last_name)

class Bill(models.Model):
    client       = models.ForeignKey(Client, null=False, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=150, verbose_name="Nombre de la compañia")
    nit          = models.CharField(max_length=15, verbose_name="NIT", help_text="Número de identificación tributaria")
    code         = models.CharField(max_length=150)

    def __str__(self):
        return str(self.company_name)


class Product(models.Model):
    name        = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    description = models.CharField(max_length=350, verbose_name="Descripción del Producto")
    attribute   = models.CharField(max_length=350)

    def __str__(self):
        return str(self.description)

class BillProduct(models.Model):
    bill        = models.ForeignKey(Bill, null=False, on_delete=models.CASCADE)
    product     = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.bill)