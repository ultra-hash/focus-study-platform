from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="api.home"),
    path('path/<str:path_name>/', views.path, name="api.path"),
]
