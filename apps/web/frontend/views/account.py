from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("用户列表")


def create(request: HttpRequest) -> HttpResponse:
    return HttpResponse("新建用户页面")


def store(request: HttpRequest) -> HttpResponse:
    return HttpResponse("新建用户")


def show(request: HttpRequest, uuid: str) -> HttpResponse:
    return HttpResponse(f"用户详情：{uuid}")


def update(request: HttpRequest, uuid: str) -> HttpResponse:
    return HttpResponse(f"编辑用户：{uuid}")


def destroy(request: HttpRequest, uuid: str) -> HttpResponse:
    return HttpResponse(f"删除用户：{uuid}")

