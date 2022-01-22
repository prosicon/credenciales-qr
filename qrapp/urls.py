from django.urls import path
from . import views

app_name = 'qrapp'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('<str:prm>/', views.index, name='index'),
]

handler404 = "qrapp.views.manejar_not_found"
