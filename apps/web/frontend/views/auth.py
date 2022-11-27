from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def get_login(request: HttpRequest) -> HttpResponse:
    return render(request, 'web/frontend/auth/login.html')


def post_login(request: HttpRequest) -> HttpResponse:
    pass


def get_register(request: HttpRequest) -> HttpResponse:
    return render(request, 'web/frontend/auth/register.html')


def post_register(request: HttpRequest) -> HttpResponse:
    pass
