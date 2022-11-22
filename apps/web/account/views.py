from django.http import HttpResponse, HttpRequest

# Create your views here.
from django.urls import reverse


def index(request: HttpRequest) -> HttpResponse:
    resolver_match = request.resolver_match
    print(f'{resolver_match.namespace}:{resolver_match.url_name}')
    return HttpResponse(reverse('apps.web.account:index'))


def show(request: HttpRequest, uuid: int) -> HttpResponse:
    return HttpResponse(reverse('apps.web.account:show', kwargs={'uuid': uuid}))


def article(request: HttpRequest, uid: int) -> HttpResponse:
    return HttpResponse(reverse('apps.web.account:article', kwargs={'uid': uid}))
