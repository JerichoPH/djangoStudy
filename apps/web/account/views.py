from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('用户列表')


def show(request: HttpRequest, uuid: int) -> HttpResponse:
    return HttpResponse(f'用户详情:{uuid}')


def article(request: HttpRequest, uid: int) -> HttpResponse:
    return HttpResponse(f'文章：{uid}')
