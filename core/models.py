from django.db import models
from django.contrib.auth.base_user import BaseUserManager


class Paciente(models.Model, BaseUserManager):
    use_in_migrations = True

    escolha_sexo=(
        ("M","Masculino"),
        ("F","Feminino"),
        ("N", "Nenhuma das Opções")
    )

    nome_paciente=models.CharField(max_length=250, blank=False, verbose_name='Nome do paciente')

    data_nascimento=models.DateField(blank=False,verbose_name='Data de Nascimento')
    sexo=models.CharField(max_length=1, choices=escolha_sexo, blank=False, null=False)
    email=models.EmailField(max_length=60, blank=False, verbose_name='E-mail', unique=True)
    senha=models.CharField(max_length= 20,blank=False)
    data_criacao = models.DateTimeField(auto_now=True)

    def _create_user(self, email, senha, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(senha)
        user.save(using=self._db)
        return user

    def create_user(self, email, senha=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, senha, **extra_fields)


    class Meta:
        db_table = 'paciente'

    def __str__(self):
        return self.nome_paciente


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
