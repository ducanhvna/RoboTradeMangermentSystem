from django.urls import path

from . import views

app_name = 'robos'

urlpatterns= [
   # path('list/', views.ListView, name = 'list'),
    # path('create/', views.CreateView, name = 'create'),
    path('list_setting/', views.ListSettingView.as_view(), name = 'list_setting'),
    path('<int:setting_id>/detail_setting/', views.SettingDetailView, name = 'detail_setting'),
]
