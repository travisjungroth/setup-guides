from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin, OrderedTabularInline, OrderedInlineModelAdminMixin, \
    OrderedStackedInline

from guides import models


class GuideStepInline(OrderedTabularInline):
    model = models.GuideStep
    fields = ('step', 'optional', 'order', 'move_up_down_links')
    readonly_fields = ('order', 'move_up_down_links')
    extra = 1
    ordering = ('order', )


@admin.register(models.Guide)
class GuideAdmin(OrderedInlineModelAdminMixin, OrderedModelAdmin):
    list_display = ('id', 'title', 'slug')
    search_fields = ('slug',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = (GuideStepInline,)


class RequirementInline(OrderedTabularInline):
    model = models.Requirement
    fk_name = 'required_by'
    fields = ('requires', 'order', 'move_up_down_links')
    readonly_fields = ('order', 'move_up_down_links')
    extra = 1
    ordering = ('order',)


class ActionInline(OrderedStackedInline):
    model = models.Action
    fields = ('text', 'order', 'move_up_down_links')
    readonly_fields = ('order', 'move_up_down_links')
    extra = 1
    ordering = ('order',)


class VerificationInline(OrderedStackedInline):
    model = models.Verification
    fields = ('text', 'order', 'move_up_down_links')
    readonly_fields = ('order', 'move_up_down_links')
    extra = 1
    ordering = ('order',)


@admin.register(models.Step)
class StepAdmin(OrderedInlineModelAdminMixin, OrderedModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}
    inlines = (RequirementInline, ActionInline, VerificationInline)


@admin.register(models.Action)
class ActionAdmin(OrderedModelAdmin):
    list_display = ('id', 'text')
    list_filter = ('id', 'text')


@admin.register(models.Verification)
class VerificationAdmin(OrderedModelAdmin):
    list_display = ('id', 'text')
    list_filter = ('id', 'text')
