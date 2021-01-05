# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'specialte',
        'contact',
        'situation_geographique',
        'date_naissance',
        'localisation',
        'status',
        'date_add',
        'date_update',
    )
    list_filter = (
        'user',
        'status',
        'date_add',
        'date_update',
    )


class SocialAdmin(admin.ModelAdmin):

    list_display = (
        'lien',
        'status',
        'date_add',
        'date_update',
    )
    list_filter = (
        'status',
        'date_add',
        'date_update',
    )


class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        'titre',
        'status',
        'date_add',
        'date_update',
    )
    list_filter = (
        'status',
        'date_add',
        'date_update',
    )


class CategorieAdmin(admin.ModelAdmin):

    list_display = ('titre', 'status', 'date_add', 'date_update')
    list_filter = (
        'status',
        'date_add',
        'date_update',
    )


class CompetenceAdmin(admin.ModelAdmin):

    list_display = (
        'categorie',
        'titre',
        'niveau',
        'status',
        'date_add',
        'date_update',
    )
    list_filter = (
        'categorie',
        'status',
        'date_add',
        'date_update',
    )


class ProjetAdmin(admin.ModelAdmin):

    list_display = ('fichier', 'status', 'date_add', 'date_update')
    list_filter = (
        'status',
        'date_add',
        'date_update',
    )


class ExperienceCategorieAdmin(admin.ModelAdmin):

    list_display = (
        'titre',
        'status',
        'date_add',
        'date_update',
    )
    list_filter = (
        'status',
        'date_add',
        'date_update',
    )


class ExperienceAdmin(admin.ModelAdmin):

    list_display = (
        'experience',
        'structure',
        'poste',
        'annee_debut',
        'annee_fin',
        'status',
        'date_add',
        'date_update',
    )
    list_filter = (
        'status',
        'date_add',
        'date_update',
    )


class ContactAdmin(admin.ModelAdmin):

    list_display = (
        'nom',
        'prenom',
        'email',
        'message',
        'status',
        'date_add',
        'date_update',
    )
    list_filter = (
        'status',
        'date_add',
        'date_update',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Profile, ProfileAdmin)
_register(models.Social, SocialAdmin)
_register(models.Service, ServiceAdmin)
_register(models.Categorie, CategorieAdmin)
_register(models.Competence, CompetenceAdmin)
_register(models.Projet, ProjetAdmin)
_register(models.ExperienceCategorie, ExperienceCategorieAdmin)
_register(models.Experience, ExperienceAdmin)
_register(models.Contact, ContactAdmin)
