from django.db import models


# Create your models here.
class Cargo(models.Model):
    id = models.AutoField(
        primary_key=True,
        null=False
    )
    criado_em = models.DateField(
        auto_now_add=True,
        null=False
    )
    modificado_em = models.DateField(
        auto_now_add=True,
        null=False
    )
    active = models.BooleanField(
        default=True,
        null=False
    )
    nome = models.CharField(
        max_length=104,
        null=False
    )

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'cargo'
        managed = True


class Funcionario(models.Model):
    class Sexo(models.TextChoices):
        MASCULINO = 'M', 'MASCULINO'
        FEMININO = 'F', 'FEMININO'

    id = models.AutoField(
        primary_key=True,
        null=False
    )
    criado_em = models.DateField(
        auto_now_add=True,
        null=False
    )
    modificado_em = models.DateField(
        auto_now_add=True,
        null=False
    )
    active = models.BooleanField(
        default=True,
        null=False
    )
    cargo = models.ForeignKey(
        to='Cargo',
        on_delete=models.DO_NOTHING,
        db_column='id_cargo',
        null=False
    )
    nome = models.CharField(
        max_length=104,
        null=False
    )
    sexo = models.CharField(
        max_length=1,
        choices=Sexo.choices,
        null=False
    )
    salario = models.DecimalField(
        decimal_places=2,
        max_digits=8,
        null=False
    )

    class Meta:
        db_table = 'funcionario'
        managed = True
