"""djangoStudy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .views import auth as auth_view
from .views import account as account_view

urlpatterns = [
    # 权鉴
    path("auth/login/", view=auth_view.get_login, name="__auth__get_login"),
    path("auth/reigster/", view=auth_view.get_register, name="__auth__get_register"),

    # 用户
    path("account/", view=account_view.index, name="__account__index"),
    path("account/create/", view=account_view.create, name="__account__create"),
    path("account/store/", view=account_view.store, name="__account__store"),
    path("account/<str:uuid>/", view=account_view.show, name="__account__show"),
    path("account/<str:uuid>/update", view=account_view.update, name="__account__update"),
    path("account/<str:uuid>/destroy", view=account_view.destroy, name="__account__destroy"),
]
