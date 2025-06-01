from django.db import models
from django.contrib.auth.models import AbstractUser

class Livro(models.Model):
    nome = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano = models.IntegerField()

    def __str__(self):  #definição de função adionada
        return f"{self.nome} - {self.autor}" 
    
class TCC(models.Model):    # classe adiconada
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    orientador = models.CharField(max_length=255)
    ano = models.IntegerField()

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
    


class Usuario(AbstractUser):
    nome = models.CharField(max_length=100)
    # O campo `email` já existe no AbstractUser (mas pode ser sobrescrito se quiser torná-lo obrigatório/único)
    # O campo `password` também já existe e é gerenciado com hash, não precisa do `senha_hash`

    def __str__(self):
        return self.username  # ou self.nome, se preferir


class Conta(models.Model):
    TIPO_CHOICES = [
        ('corrente', 'Conta Corrente'),
        ('poupanca', 'Poupança'),
        ('investimento', 'Investimento'),
    ]

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    saldo_inicial = models.FloatField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='contas')

    def __str__(self):
        return f"{self.nome} ({self.tipo})"


class Categoria(models.Model):
    TIPO_CHOICES = [
        ('receita', 'Receita'),
        ('despesa', 'Despesa'),
    ]

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    def __str__(self):
        return f"{self.nome} ({self.tipo})"


class Transacao(models.Model):
    TIPO_CHOICES = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    ]

    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    descricao = models.CharField(max_length=255)
    valor = models.FloatField()
    data = models.DateField()
    forma_pagamento = models.CharField(max_length=50)
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='transacoes')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='transacoes')

    def __str__(self):
        return f"{self.tipo} - {self.valor} em {self.data}"


class Meta(models.Model):
    categoria = models.CharField(max_length=100)
    valor_limite = models.FloatField()
    periodo = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='metas')

    def __str__(self):
        return f"Meta de {self.categoria} - {self.valor_limite}"


class Alerta(models.Model):
    mensagem = models.TextField()
    data = models.DateField()
    visualizado = models.BooleanField(default=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='alertas')

    def __str__(self):
        return f"Alerta: {self.mensagem[:30]}..."