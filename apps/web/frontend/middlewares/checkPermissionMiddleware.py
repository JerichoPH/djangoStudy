from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpRequest, HttpResponse


class CheckPermissionMiddleware(MiddlewareMixin):
    _white_list = [
        "apps.web.frontend:__auth__get_login",  # 登录页面
        "apps.web.frontend:__auth__post_login",  # 登录
        "apps.web.frontend:__auth__get_register",  # 注册页面
        "apps.web.frontend:__auth__post_register",  # 注册
    ]

    def process_request(self, request: HttpRequest):
        pass

    def process_view(self, request: HttpRequest, view_func, view_args: list, view_kwargs: dict):

        resolver_match = request.resolver_match
        resolver_match_namespace = resolver_match.namespace
        resolver_match_url_name = resolver_match.url_name
        resolver_route_name = f"{resolver_match_namespace}:{resolver_match_url_name}"

        if not resolver_route_name in self._white_list:
            # 获取用户信息
            auth = request.session.auth
            # 检查用户拥有权限是否具备当前权限
            # ...
            has_prermission = False
            if not has_prermission:
                return HttpResponse("无权操作")
        pass

    def process_response(self, request: HttpRequest, response: HttpResponse):
        return response
