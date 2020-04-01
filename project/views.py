from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse


def heartbeat(request: HttpRequest) -> HttpResponse:
    return HttpResponse(status=200)


class Home(TemplateView):
    template_name = 'home.html'
