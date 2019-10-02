from django.db import models
from django.db.models import CharField


class Contato(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Livraria(models.Model):
    Titulo = models.CharField(max_length=50)
    Nome_do_autor = models.CharField(max_length=200)
    Assunto = models.CharField(max_length=50)
    Editora = models.CharField(max_length=50)
    ISBN = models.CharField(max_length=50)
    Ano_da_publicacao = models.DateField()

    def __str__(self):
        return self.Titulo


class Despesa(models.Model):
    Data_criacao = models.CharField(max_length=50)
    Tipo_despesa = models.CharField(max_length=200)
    descricao = models.CharField(max_length=50)
    forma_pagamento = models.CharField(max_length=50)
    vencimento = models.DateField()
    quitado = models.BooleanField()

    def __str__(self):
        return self.Data_criacao

class Compras (models.Model):
    nome = models.CharField(max_length=50)
    descricaoProduto = models.CharField(max_length=100)
    unidadeCompra = models.CharField(max_length=50)
    qtdPrevistoMes = models.FloatField()
    preco = models.FloatField()
    precoMaximo = models.FloatField()

    def __str__(self):
        return Self.nome

class Apartamento(models.Model):
    numero = models.IntegerField()
    qtdQuarto = models.IntegerField()
    proprietario = models.CharField(max_length=50)
    valorCondominio= models.FloatField()


    def __str__(self):
        return Self.numero


class Anuncio(models.Model):
    cliente = models.CharField(max_length=100)
    texteTitulo = models.CharField(max_length=50)
    preço = models.FloatField()
    textoAnuncio = models.FloatField()
    nomeContado=models.CharField(max_length=50)
    telefone =models.CharField(max_length=50)
    secao=models.CharField(max_length=50)
    tipoAnuncio=models.CharField(max_length=50)

    def __str__(self):
        return Self.cliente
    
class Autor (models.Moldels):
    class Meta:
        verbose_nome_plural='autores'
        nome=modelos.ChartField(max_length=50)
        sobrenome = models.CharField(max_length=50)
    def __str__(self):
        return self.sobrenome.upper()+','+ self.nome
class Aluno(models.Model):
    matricula = models.CharField(max_length=12,unique= True)
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    email =models.EmailField(max_length=100)
    def __str__(self):
        return  self.nome
class Livro(models.Model):
    titulo=models.CharField(max_length=100)
    ano_publicao=models.IntegerField()
    def __str__(self):
        return "{},({})".format(self.titulo,self.ano_publicao)
class Emprestimo (models.Model):
    usuario=models.ForeignKey('auth.user',on_delete= models.CASCADE)
    aluno = models.ForeignKey(Aluno,on_delete= models.CASCADE)
    data_devolucao= moldels.DateField()
    livros = models.ManyToManyField(Livro)
    devolvido = models.BooleanField() 
