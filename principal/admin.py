from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']


@admin.register(models.Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    pass
