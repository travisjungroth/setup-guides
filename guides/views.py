from django.views.generic import DetailView

from guides.models import Guide


class GuideDetail(DetailView):
    model = Guide

