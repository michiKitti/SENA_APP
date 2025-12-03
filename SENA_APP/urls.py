from django.contrib import admin
from django.urls import include, path
from aprendices import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aprendices.urls')),
    path('instructores/', include('instructores.urls')),
    path('programas/', include('programas.urls')),
 
]
