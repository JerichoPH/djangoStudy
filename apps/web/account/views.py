from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.decorators.http import require_http_methods
# Create your views here.
from django.urls import reverse


@require_http_methods(['GET'])
def get_login(request: HttpRequest) -> HttpResponse:
    content = render_to_string('web/account/login.html', None, request, using=None)
    resp = HttpResponse(content)
    resp['a'] = 'aaa'
    return resp


@require_http_methods(['POST'])
def post_login(request: HttpRequest) -> HttpResponse:
    print(request.COOKIES)
    return JsonResponse(data={'msg': 'test'})


def index(request: HttpRequest) -> HttpResponse:
    resolver_match = request.resolver_match
    print(f'{resolver_match.namespace}:{resolver_match.url_name}')
    return HttpResponse(reverse('apps.web.account:index'))


def show(request: HttpRequest, uuid: int) -> HttpResponse:
    return HttpResponse(reverse('apps.web.account:show', kwargs={'uuid': uuid}))


def article(request: HttpRequest, uid: int) -> HttpResponse:
    return HttpResponse(reverse('apps.web.account:article', kwargs={'uid': uid}))
