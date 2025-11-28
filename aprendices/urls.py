from django.urls import path
from . import views 
app_name = 'aprendices' 
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('aprendices/', views.aprendices, name='lista_aprendices'),
    path('aprendices/<int:id_aprendiz>/', views.detalle_aprendiz, name='detalle_aprendiz'),
]