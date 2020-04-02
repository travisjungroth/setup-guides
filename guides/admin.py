from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin, OrderedTabularInline

from guides import models


class GuideStepTabularInline(OrderedTabularInline):
    model = models.GuideStep
    fields = ('step', 'optional', 'order', 'move_up_down_links')
    readonly_fields = ('order', 'move_up_down_links')
    extra = 1
    ordering = ('order', )


@admin.register(models.Guide)
class GuideAdmin(OrderedModelAdmin):
    list_display = ('id', 'title', 'slug')
    search_fields = ('slug',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = (GuideStepTabularInline, )


@admin.register(models.Step)
class StepAdmin(OrderedModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')
    # raw_id_fields = ('requirements', 'actions', 'verifications')


@admin.register(models.Action)
class ActionAdmin(OrderedModelAdmin):
    list_display = ('id', 'text')
    list_filter = ('id', 'text')


@admin.register(models.Verification)
class VerificationAdmin(OrderedModelAdmin):
    list_display = ('id', 'text')
    list_filter = ('id', 'text')
