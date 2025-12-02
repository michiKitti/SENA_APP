from django.contrib import admin
from django.urls import include, path
from aprendices import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Ruta para aprendices
    path('', include('aprendices.urls')),

    # Ruta para instructores
    path('instructores/', views.lista_instructores, name='lista_instructores'),
]
