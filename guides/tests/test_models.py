from pytest import mark


@mark.django_db
def test_guide_create(guide_factory):
    guide_factory()


@mark.django_db
def test_step_create(step_factory):
    step_factory()


@mark.django_db
def test_action_create(action_factory):
    action_factory()


@mark.django_db
def test_verification_create(verification_factory):
    verification_factory()
