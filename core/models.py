import math

from django.db import models

#Models definem a estrutura dos dados armazenados, classes, campos e como eles se comportam
#depois de fazer as migracoes as classes python serao convertidas em SQL


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)

    def __str__(self): # permite que eu escolha a string que aparece quando chamo a classe na tela
        return self.nome


class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self): # permite que eu escolha a string que aparece quando chamo a classe na tela
        return self.nome


class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)  # campo dessa é a classe acima
    placa = models.CharField(max_length=7)
    proprietario = models.ForeignKey(Pessoa, on_delete=models.CASCADE, default=1)
    cor = models.CharField(max_length=14)
    observacoes = models.TextField()

    def __str__(self): # permite que eu escolha a string que aparece quando chamo a classe na tela
        return  self.proprietario.nome + " | " +  self.placa



class Parametro(models.Model):
    periodo = models.CharField(max_length=29)
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.periodo


class MovRotativo(models.Model):
    checkin = models.DateTimeField(auto_now=False)
    checkout = models.DateTimeField(auto_now=False, null=True, blank=True)
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)#mudar para depois puxar sozinho dos parametros
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    pago = models.BooleanField(default=False)

    def horas_total(self):
        return math.ceil((self.checkout - self.checkin).total_seconds() / 3600)
    def total(self):
        if self.checkout is None:
            return "A definir"
        return self.valor_hora * self.horas_total()
    def __str__(self):
        return self.veiculo.placa

class Mensalista(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    inicio = models.DateField()
    valor_mes = models.DecimalField(max_digits= 8, decimal_places=2)

    def __str__(self):
        return self.veiculo.proprietario.nome + " | "+self.veiculo.placa

class MovMensalista(models.Model):
    mensalista = models.ForeignKey(Mensalista, on_delete=models.CASCADE)
    data_pgto = models.DateField()
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.mensalista) + "  | R$" + str(self.total)
