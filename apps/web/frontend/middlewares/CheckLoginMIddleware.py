from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpRequest, HttpResponse


class CheckLoginMiddleware(MiddlewareMixin):

    def process_request(self, request: HttpRequest):
        if not hasattr(request.session, "auth"):
            return redirect(reverse("apps.web.frontend:__auth__get_login"))

    def process_view(self, request: HttpRequest, view_func, view_args: list, view_kwargs: dict):
        pass

    def process_response(self, request: HttpRequest, response: HttpResponse):
        pass
