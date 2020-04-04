from django.views.generic import DetailView, ListView

from guides.models import Guide, Step


class GuideDetail(DetailView):
    model = Guide

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class GuideList(ListView):
    model = Guide


class StepDetail(DetailView):
    model = Step


class StepList(ListView):
    model = Step
