from django.urls import path
from abrigos.views import abrigos_view

urlpatterns = [
    path('', abrigos_view),
]