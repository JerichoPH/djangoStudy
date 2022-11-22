from django.urls import path

from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('<int:uuid>/', view=views.show, name='show'),
    path('<int:uid>/article/', view=views.article, name='article'),
]
