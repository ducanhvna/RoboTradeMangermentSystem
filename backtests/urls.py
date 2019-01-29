from django.urls import path

from . import views

app_name = 'backtests'

urlpatterns= [
    path('list/', views.ListBackTestView.as_view(), name = 'list'),
    path('create/', views.CreateBackTestView.as_view(), name = 'create'),
    path('<int:pk>/edit/', views.EditBackTestView.as_view(), name = 'edit'),
    path('<int:pk>/view/', views.BackTestDetailView.as_view(), name="view_BackTest"),
    path('setting/add', views.CreateBackTestSettingView.as_view(), name = 'add_setting'),
]
