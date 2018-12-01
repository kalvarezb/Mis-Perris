from django.contrib import admin
from .models import Rescatado
from .models import Adoptante

admin.site.register(Rescatado)
admin.site.register(Adoptante)