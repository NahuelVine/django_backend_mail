from django.contrib import admin

# Register your models here.
from .forms import RegModelForm
from .models import Registrado

class AdminRegistrado(admin.ModelAdmin):
    list_display = ["email", "nombre", "timeStamp"]
    form = RegModelForm
    #list_display_links = ["nombre"]
    list_filter = ["timeStamp"]
    list_editable = ["nombre"]
    search_fields = ["email" , "nombre"]
    #class Meta:
    #    model = Registrado


admin.site.register(Registrado, AdminRegistrado)