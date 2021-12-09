from django.contrib import admin
from .models import Restauracja
from .models import Danie
from .models import Zamowienie
from .models import Szczegoly

# Register your models here.
admin.site.register(Restauracja)
admin.site.register(Danie)
admin.site.register(Zamowienie)
admin.site.register(Szczegoly)