from django.contrib import admin

from guides import models


@admin.register(models.Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_filter = ('id', 'title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('steps',)
    search_fields = ('slug',)


@admin.register(models.Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')
    # raw_id_fields = ('requirements', 'actions', 'verifications')


@admin.register(models.Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_filter = ('id', 'text')


@admin.register(models.Verification)
class VerificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_filter = ('id', 'text')
