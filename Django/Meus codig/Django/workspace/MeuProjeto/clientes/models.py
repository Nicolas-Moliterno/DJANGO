from django.db import models

# Create your models here.



class CPF(models.Model):
    numero = models.CharField(max_length=15)  
    data_exp = models.DateTimeField(auto_now=False)
    def __str__(self):
        return self.numero



class Empregado(models.Model):
    nome = models.CharField(max_length=70,blank=True, null=False)
    endereco = models.CharField(max_length=200, blank=True, null=False)   
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    idade = models.IntegerField()
    email = models.EmailField()     
    cpf = models.OneToOneField(CPF,blank=True, null=True, on_delete=models.PROTECT)
    foto = models.ImageField(upload_to='clientes_fotos')



    def __str__(self):
        return self.nome


class Telefone(models.Model):
    numero = models.CharField(max_length=20)
    descricao = models.CharField(max_length=80)
    Empregado = models.ForeignKey(Empregado,on_delete=models.PROTECT)

    def __str__(self):
        return self.numero + " - " + self.descricao

