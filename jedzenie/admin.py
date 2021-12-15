from django.contrib import admin

from .models import Danie, Restauracja, Szczegoly, Zamowienie

# Register your models here.
admin.site.register(Restauracja)
admin.site.register(Danie)
admin.site.register(Zamowienie)
admin.site.register(Szczegoly)
