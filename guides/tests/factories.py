import factory

from guides import models


class GuideFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Guide

    title = factory.Sequence(lambda n: f'Guide {n}')


class StepFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Step

    title = factory.Sequence(lambda n: f'Guide {n}')


class ActionFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Action

    step = factory.SubFactory(StepFactory)


class VerificationFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Verification

    step = factory.SubFactory(StepFactory)
