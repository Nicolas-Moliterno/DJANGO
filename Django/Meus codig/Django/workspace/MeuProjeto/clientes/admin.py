from django.contrib import admin
from .models import Empregado,Telefone,CPF


# Register your models here.

class EmpregadoAdmin(admin.ModelAdmin):
    fields = ('nome','endereco')
    list_display = ('id','nome','endereco','email')
    search_field = ('id','nome')

admin.site.register(Empregado,EmpregadoAdmin)
admin.site.register(Telefone)
admin.site.register(CPF)
