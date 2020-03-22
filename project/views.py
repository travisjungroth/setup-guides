from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'home.html'


def trigger_error(request):
    return 1 / 0
