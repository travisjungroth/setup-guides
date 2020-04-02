from django.db import models
from ordered_model.models import OrderedModel


class Guide(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    steps = models.ManyToManyField('Step', through='GuideStep', blank=True)


class GuideStep(OrderedModel):
    guide = models.ForeignKey('Guide', on_delete=models.CASCADE)
    step = models.ForeignKey('Step', on_delete=models.CASCADE)
    optional = models.BooleanField(default=False)
    order_with_respect_to = 'guide'


class Step(models.Model):
    title = models.CharField(max_length=255)
    requirements = models.ManyToManyField('self', through='Requirement', symmetrical=False, blank=True)


class Requirement(OrderedModel):
    required_by = models.ForeignKey('Step', related_name='+', on_delete=models.CASCADE)
    requires = models.ForeignKey('Step', related_name='+', on_delete=models.CASCADE)
    order_with_respect_to = 'required_by'


class Action(OrderedModel):
    text = models.TextField()
    step = models.ForeignKey(Step, related_name='actions', on_delete=models.CASCADE)
    order_with_respect_to = 'step'


class Verification(OrderedModel):
    text = models.TextField()
    step = models.ForeignKey('Step', related_name='verifications', on_delete=models.CASCADE)
    order_with_respect_to = 'step'
