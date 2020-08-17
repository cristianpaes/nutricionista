from django.contrib import admin
from core.models import *

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    model = Paciente
    list_display = ['nome_paciente', 'usuario','data_nascimento', 'sexo', 'email']
    list_per_page = 5

@admin.register(Refeicao)
class RefeicaoAdmin(admin.ModelAdmin):
    list_display = ['nome_ref']

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ['id','nome_receita','descricao', 'tipo_ref', 'tag']

@admin.register(Prescricao)
class PrescricaoAdmin(admin.ModelAdmin):
    list_display = ['id','ref_paciente','data_presc', 'peso', 'ref_receita','observacao']