from django.urls import path

from . import views

urlpatterns = [
    path('', view=views.index, name='account.index'),
    path('<uuid>/', view=views.show, name='account.show'),
    path('<uid>/article/', view=views.article, name='account.article'),
]
