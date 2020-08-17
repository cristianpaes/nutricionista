from django.db import models
from django.contrib.auth.models import User

class Paciente(models.Model):

     escolha_sexo=(
         ("M","Masculino"),
         ("F","Feminino"),
         ("N", "Nenhuma das Opções")
     )

     usuario = models.OneToOneField(User, on_delete=models.CASCADE)
     nome_paciente=models.CharField(max_length=250, blank=False, verbose_name='Nome do paciente')
     data_nascimento=models.DateField(blank=False,verbose_name='Data de Nascimento')
     sexo=models.CharField(max_length=1, choices=escolha_sexo, blank=False, null=False)
     email=models.EmailField(max_length=60, blank=False, verbose_name='E-mail', unique=True)
     data_criacao = models.DateTimeField(auto_now=True)

     class Meta:
         db_table = 'paciente'

     def __str__(self):
         return self.User.name


class Refeicao(models.Model):
    nome_ref=models.CharField(max_length=250, blank=False,verbose_name='Refeição')

    class Meta:
        db_table = 'refeicao'
        ordering = ['id']

    def __str__(self):
        return self.nome_ref

class Receita(models.Model):
    nome_receita=models.CharField(max_length=100, blank=False, verbose_name='Receita')
    descricao= models.TextField(blank=False)
    tipo_ref=models.ForeignKey(Refeicao, on_delete= models.DO_NOTHING, verbose_name='Tipo da Refeição')
    tag=models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'receita'

    def __str__(self):
        return self.nome_receita

class Prescricao(models.Model):
    ref_paciente=models.ForeignKey(Paciente, blank=False, on_delete= models.DO_NOTHING, verbose_name='Paciente' )
    data_presc=models.DateField(verbose_name='Data da Prescrição')
    peso=models.DecimalField(max_digits=3, decimal_places=2)
    ref_receita=models.ForeignKey(Receita, blank=False, on_delete= models.DO_NOTHING, verbose_name='Receita')
    observacao= models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'prescricao'

    def __str__(self):
        return self.ref_paciente
