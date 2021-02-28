from django.contrib import admin
from django.conf.urls import url
from django.conf import settings
from django.urls import path, include
from django.templatetags.static import static
from django.conf.urls.static import static
from .views import (
    home,
    contato,
    servico,
)


urlpatterns = [
    path('',home, name='website_home'),
    path('contato',contato, name='website_contato'),
    path('servico',servico, name='website_servico'),
    path('',home, name='core_home'),
    

] 


