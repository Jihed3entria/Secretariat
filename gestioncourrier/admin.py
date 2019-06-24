# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Courrier, CourrierR, justificatif


# Register your models here.

class AdminCourrier(admin.ModelAdmin):
    list_display = ('objet', 'expediteur', 'nom', 'surnom', 'destinataire', 'dateArrive', 'piece_jointe')
    list_filter = ('objet', 'expediteur', 'dateArrive')
    search_fields = ('objet', 'nom', 'surnom', 'dateArrive', 'expediteur')


admin.site.register(Courrier, AdminCourrier)


class AdminCourrierR(admin.ModelAdmin):
    list_display = ('objet', 'nom', 'surnom', 'dateArrive', 'Nbr')
    list_filter = ('objet', 'dateArrive', 'expediteur')
    search_fields = ('nom', 'surnom', 'objet', 'dateArrive')


admin.site.register(CourrierR, AdminCourrierR)


class AdminJustificatif(admin.ModelAdmin):
    list_display = ('nom', 'surnom', 'dateArrive', 'parcours','valide')
    list_filter = ('dateArrive', 'parcours')
    search_fields = ('nom', 'surnom', 'parcours', 'dateAbsence', 'dateJustification')


admin.site.register(justificatif, AdminJustificatif)
