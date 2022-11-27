from django.urls import path

from . import views

urlpatterns = [
    path('login', view=views.get_login, name='get_login'),
    path('register', view=views.get_register, name='get_register'),
    path('', view=views.index, name='index'),
    path('<int:uuid>/', view=views.show, name='show'),
    path('<int:uid>/article/', view=views.article, name='article'),
]
