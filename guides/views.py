from django.views.generic import DetailView, ListView

from guides.models import Guide, Step


class GuideDetail(DetailView):
    model = Guide


class GuideList(ListView):
    model = Guide


class StepDetail(DetailView):
    model = Step


class StepList(ListView):
    model = Step
