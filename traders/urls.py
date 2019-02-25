from django.urls import path

from . import views

app_name = 'traders'

urlpatterns= [
    path('list/', views.ListTraderView.as_view(), name = 'list'),
    path('create/', views.CreateTraderWizardView.as_view(), name = 'create'),
    # path('<int:pk>/edit/', views.EditTraderView.as_view(), name = 'edit'),
    # path('<int:pk>/view/', views.TraderDetailView.as_view(), name="view_Trader"),
    # path('setting/add', views.CreateTraderSettingView.as_view(), name = 'add_setting'),
    # path('setting/edit', views.EditTraderSettingView.as_view(), name = 'edit_setting'),
]
