from django.contrib import admin
from .models import Dijagonala, Televizor


# Register your models here.
@admin.register(Dijagonala)
class DijagonalaAdmin(admin.ModelAdmin):
    list_display = ['naziv', 'slug']
    prepopulated_fields = {'slug': ('naziv',)}


@admin.register(Televizor)
class TelevizorAdmin(admin.ModelAdmin):
    list_display = ['naziv', 'slug', 'cena', 'raspoloziv', 'kreiran', 'azuriran']
    list_filter = ['raspoloziv', 'kreiran', 'azuriran']
    list_editable = ['cena', 'raspoloziv']
    prepopulated_fields = {'slug': ('naziv',)}
