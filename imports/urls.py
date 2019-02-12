from django.urls import path
from . import views

app_name= 'imports'

urlpatterns = [
    path('backtest', views.ImportTimeline, name='import_backtest'),
]