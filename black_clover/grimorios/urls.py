from django.urls import path

from black_clover.grimorios.views import (
    GetAllGrimorios,
    GetAllRegistration,
    Register,
    UpdateStatus,
)

urlpatterns = [
    path("register/", Register.as_view(), name="register"),
    path("register/<uuid:uuid>/", Register.as_view(), name="register"),
    path("registration/", GetAllRegistration.as_view(), name="registration"),
    path("grimorios/", GetAllGrimorios.as_view(), name="grimorios"),
    path("update_status/<uuid:uuid>/", UpdateStatus.as_view(), name="grimorios"),
]
