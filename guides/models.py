from django.db import models


class Guide(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    # steps = SortedManyToManyField('Step', blank=True)


class Step(models.Model):
    title = models.CharField(max_length=255)
    requirements = models.ManyToManyField('Step')
    actions = models.ForeignKey('Action', blank=True, on_delete=models.PROTECT)
    # verifications = SortedManyToManyField('Verification', blank=True)


class Action(models.Model):
    text = models.TextField()


class Verification(models.Model):
    text = models.TextField()
