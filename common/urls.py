from django.urls import path
from . import views

app_name='common'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
]
