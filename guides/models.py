from django.db import models
from ordered_model.models import OrderedModel


class Guide(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    # steps = SortedManyToManyField('Step', blank=True)


class Step(models.Model):
    title = models.CharField(max_length=255)
    requirements = models.ManyToManyField('Step')
    # verifications = SortedManyToManyField('Verification', blank=True)


class Action(OrderedModel):
    text = models.TextField()
    step = models.ForeignKey(Step, on_delete=models.PROTECT)
    order_with_respect_to = 'step'


class Verification(models.Model):
    text = models.TextField()
