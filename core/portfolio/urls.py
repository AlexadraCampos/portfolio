from django.contrib import admin
from django.urls import path
from core import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('contato/', views.contato, name='contato'),
    path('sobre/', views.sobre_mim, name='sobre_mim'),
    path('projetos/', views.projetos, name='projetos'),

]
