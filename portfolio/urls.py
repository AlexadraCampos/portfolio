from django.contrib import admin
from django.urls import path
from . import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('index/', views.home, name='index'),
    path('contato/', views.contato, name='contato'),
    path('sobre/', views.sobre_mim, name='sobre_mim'),
    path('projetos/', views.projetos, name='projetos'),

]
