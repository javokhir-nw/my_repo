from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from store.views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('single/<int:pk>/', single, name = 'single'),
    path('product/<slug>', products, name = 'products'),
]
