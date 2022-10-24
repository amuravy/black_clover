from django.urls import path

from black_clover.grimorios.views import GetAllGrimorios, GetAllRegistration, Register

urlpatterns = [
    path("register/", Register.as_view(), name="register"),
    path("register/<uuid:uuid>/", Register.as_view(), name="register"),
    path("registration/", GetAllRegistration.as_view(), name="registration"),
    path("grimorios/", GetAllGrimorios.as_view(), name="grimorios"),
]
