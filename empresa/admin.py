from django.contrib import admin
from models import *


admin.site.register(Funcionario, Funcionario.Admin)
admin.site.register(Departamento)