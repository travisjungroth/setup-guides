from django.views.generic import DetailView

from guides.models import Guide, Step


class GuideDetail(DetailView):
    model = Guide


class StepDetail(DetailView):
    model = Step
