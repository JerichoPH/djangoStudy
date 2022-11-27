from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
# Create your views here.
from django.urls import reverse


def get_login(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        template_name="web/account/login.html",
        context={
            "data": [
                {"name": "张三", "age": 18},
                {"name": "李四", "age": 28},
                {"name": "王五", "age": 38},
                {"name": "赵六", "age": 48},
                {"name": "张三", "age": 18},
                {"name": "李四", "age": 28},
                {"name": "王五", "age": 38},
                {"name": "赵六", "age": 48},
                {"name": "张三", "age": 18},
                {"name": "李四", "age": 28},
                {"name": "王五", "age": 38},
                {"name": "赵六", "age": 48},
                {"name": "张三", "age": 18},
                {"name": "李四", "age": 28},
                {"name": "王五", "age": 38},
                {"name": "赵六", "age": 48},
                {"name": "张三", "age": 18},
                {"name": "李四", "age": 28},
                {"name": "王五", "age": 38},
                {"name": "赵六", "age": 48},
                {"name": "张三", "age": 18},
                {"name": "李四", "age": 28},
                {"name": "王五", "age": 38},
                {"name": "赵六", "age": 48},
                {"name": "张三", "age": 18},
                {"name": "李四", "age": 28},
                {"name": "王五", "age": 38},
                {"name": "赵六", "age": 48},
                {"name": "张三", "age": 18},
                {"name": "李四", "age": 28},
                {"name": "王五", "age": 38},
                {"name": "赵六", "age": 48},
                {"name": "张三", "age": 18},
                {"name": "李四", "age": 28},
                {"name": "王五", "age": 38},
                {"name": "赵六", "age": 48},
                {"name": "张三", "age": 18},
                {"name": "李四", "age": 28},
                {"name": "王五", "age": 38},
                {"name": "赵六", "age": 48},
                {"name": "张三", "age": 18},
                {"name": "李四", "age": 28},
                {"name": "王五", "age": 38},
                {"name": "赵六", "age": 48},
                {"name": "张三", "age": 18},
                {"name": "李四", "age": 28},
                {"name": "王五", "age": 38},
                {"name": "赵六", "age": 48},
            ],
            "a": [0, 1, 2, 3]
        }
    )


def get_register(request: HttpRequest) -> HttpResponse:
    return render(request, template_name='web/account/register.html')


def index(request: HttpRequest) -> HttpResponse:
    resolver_match = request.resolver_match
    print(f"{resolver_match.namespace}:{resolver_match.url_name}")
    return HttpResponse(reverse("apps.web.account:index"))


def show(request: HttpRequest, uuid: int) -> HttpResponse:
    return HttpResponse(reverse("apps.web.account:show", kwargs={"uuid": uuid}))


def article(request: HttpRequest, uid: int) -> HttpResponse:
    return HttpResponse(reverse("apps.web.account:article", kwargs={"uid": uid}))
