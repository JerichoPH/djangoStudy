import math
from typing import Any
from urllib.parse import urlencode

from django import template
from django.http import HttpRequest

register = template.Library()


@register.simple_tag
def add(value, num=1):
    return value + num


@register.simple_tag
def cut(value, num=1):
    return value - num


@register.simple_tag
def times(value, num=2):
    return value * num


@register.inclusion_tag("web/account/paginator.html")
def paginator(request: HttpRequest, data: Any):
    request_get = request.GET.dict()
    page_size = int(request_get.get("page_size") or 1)
    page_current = int(request_get.get("page") or 1)
    loop_times = int(request_get.get("loop_times") or 5)
    page_max = math.ceil(len(data) / page_size)

    if page_current < 1:
        page_current = 1
    if page_current > page_max:
        page_current = page_max
    page_next = page_current + 1
    if page_next > page_max:
        page_next = page_max
    page_previous = page_current - 1
    if page_previous < 1:
        page_previous = 1

    request_get["page"] = page_next
    url_next = f"{request.path}?{urlencode(request_get)}"
    request_get["page"] = page_previous
    url_previous = f"{request.path}?{urlencode(request_get)}"
    request_get["page"] = 1
    url_original = f"{request.path}?{urlencode(request_get)}"
    request_get["page"] = page_max
    url_finished = f"{request.path}?{urlencode(request_get)}"

    if loop_times <= 0:
        loop_times = 1
    loop_original = page_current - loop_times
    if loop_original < 1:
        loop_original = 1
    loop_finished = page_current + loop_times + 1
    if loop_finished > page_max:
        loop_finished = page_max + 1

    urls = {}
    for page in range(loop_original, loop_finished):
        request_get["page"] = page
        urls[page] = f"{request.path}?{urlencode(request_get)}"

    pager = {
        "page": {"current": page_current, "size": page_size, "max": page_max, },
        "url": {"next": url_next, "previous": url_previous, "original": url_original, "finished": url_finished, "loop": urls, },
    }

    return pager
