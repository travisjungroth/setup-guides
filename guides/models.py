from django.db import models
from django.urls import reverse
from ordered_model.models import OrderedModel


class Guide(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    notes = models.TextField(default='')
    steps = models.ManyToManyField('Step', through='GuideStep', blank=True)

    def get_absolute_url(self):
        return reverse('guide-detail', args=[self.slug])


class GuideStep(OrderedModel):
    guide = models.ForeignKey('Guide', on_delete=models.CASCADE)
    step = models.ForeignKey('Step', on_delete=models.CASCADE)
    optional = models.BooleanField(default=False)
    order_with_respect_to = 'guide'


class Step(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    requirements = models.ManyToManyField('self', through='Requirement', symmetrical=False, blank=True)

    def get_absolute_url(self):
        return reverse('step-detail', args=[self.slug])


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
