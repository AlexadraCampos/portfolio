from django.contrib import admin
from django.urls import path
from core import views  


urlpatterns = [
    path('admin/', admin.site.urls),  # Página do admin
    path('', views.home, name='home'),  # Página inicial (home.html)
    path('contato/', views.contato, name='contato'),  # Página de contato (contato.html)
    path('projetos/', views.projetos, name='projetos'),  # Página de projetos (projetos.html)
    path('sobre/', views.sobre_mim, name='sobre_mim'),  # Página sobre mim (sobre_mim.html)
]

