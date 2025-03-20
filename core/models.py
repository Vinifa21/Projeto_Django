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