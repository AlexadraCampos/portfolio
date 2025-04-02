from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('sobre/', views.sobre_mim, name='sobre_mim'),
    path('contato/', views.contato, name='contato'),
    path('projetos/', views.projetos, name='projetos'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
