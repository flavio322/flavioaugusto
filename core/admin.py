from django.contrib import admin
from .models import Contato
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')
admin.site.register(Contato, ContatoAdmin)

from django.contrib import admin
from .models import Livraria
class LivrariaAdmin(admin.ModelAdmin):
    list_display = ('Titulo', 'Assunto', 'Editora')
admin.site.register(Livraria, LivrariaAdmin)

from django.contrib import admin
from .models import Despesa
class DespesaAdmin(admin.ModelAdmin):
    list_display = ('Data_criacao', 'Tipo_despesa', 'descricao')
admin.site.register(Despesa, DespesaAdmin)

from django.contrib import admin
from .models import Compras
class ComprasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricaoProduto', )
admin.site.register(Compras, ComprasAdmin)

from django.contrib import admin
from .models import Apartamento
class ApartamentoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'qtdQuarto', )
admin.site.register(Apartamento, ApartamentoAdmin)

from  django.contrib import admin
from .models import Anuncio
class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'texteTitulo', )
admin.site.register(Anuncio, AnuncioAdmin)

from django.contrib import admin
from .models import  *
 class AlunoAdmin(admin.ModelAdmin):
     list_display = ('nome','matricula','data_nascimento')
     class EmprestimoAdmin(admin.ModelAdmin):
         list_display = ('data_devolucao','data_retirada','aluno','devolvido')
         filter_horizontal = ['Livros']
admin.site.register(Livro)
admin.site.register(Autor)
admin.site.register(Aluno,AlunoAdmin)
admin.site.register(Emprestimo,EmprestimoAdmin)
