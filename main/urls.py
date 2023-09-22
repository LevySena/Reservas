from django.urls import path
from main.views import *


urlpatterns = [
    path("", Reservas, name="reservas"),
]
