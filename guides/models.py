from django.db import models
from sortedm2m.fields import SortedManyToManyField


class Guide(models.Model):
    title = models.CharField(max_length=255)
    steps = SortedManyToManyField('Step')


class Step(models.Model):
    title = models.CharField(max_length=255)
    requirements = models.ManyToManyField('Step')
    actions = SortedManyToManyField('Action')
    verifications = SortedManyToManyField('Verification')


class Action(models.Model):
    text = models.TextField()


class Verification(models.Model):
    text = models.TextField()
