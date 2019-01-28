
from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns= [
  #  path('', views.index, name='index'),
    path('list/', views.ListAccountView.as_view(), name = 'list'),
    path('create/', views.CreateAccountView.as_view(), name = 'create'),
    path('<int:pk>/edit/', views.EditAccountView.as_view(), name = 'edit'),
    path('<int:pk>/detail/', views.DetailAccountView.as_view(), name = 'detail'),
]
