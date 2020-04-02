from pytest_factoryboy import register

from guides.tests.factories import GuideFactory, StepFactory, ActionFactory, VerificationFactory

register(GuideFactory)
register(StepFactory)
register(ActionFactory)
register(VerificationFactory)
