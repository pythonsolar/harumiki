from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('dashboard/', Dashboard, name='dashboard'),
    path('ghpage/', GHpage, name='ghpage'),
    path('designui/', DesignUI, name='designui'),
]