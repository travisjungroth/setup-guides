from django.contrib import admin

from . import models


class GuideAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'slug')
    list_filter = ('id', 'title', 'slug')
    raw_id_fields = ('steps',)
    search_fields = ('slug',)


class StepAdmin(admin.ModelAdmin):

    list_display = ('id', 'title')
    list_filter = ('id', 'title')
    raw_id_fields = ('requirements', 'actions', 'verifications')


class ActionAdmin(admin.ModelAdmin):

    list_display = ('id', 'text')
    list_filter = ('id', 'text')


class VerificationAdmin(admin.ModelAdmin):

    list_display = ('id', 'text')
    list_filter = ('id', 'text')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Guide, GuideAdmin)
_register(models.Step, StepAdmin)
_register(models.Action, ActionAdmin)
_register(models.Verification, VerificationAdmin)
