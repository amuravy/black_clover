import logging
from datetime import datetime

# Create your views here.
from rest_framework import status
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from black_clover.grimorios.models import Grimorio, Profile
from black_clover.grimorios.serializers import GrimorioSerializer, ProfileSerializer


class Register(APIView):
    """Register a profile."""

    def post(self, request):
        data = request.data
        AFFINITY = {
            "luz": Profile.LIGHT,
            "oscuridad": Profile.DARKNESS,
            "fuego": Profile.FIRE,
            "agua": Profile.WATER,
            "viento": Profile.WIND,
            "tierra": Profile.EARTH,
        }
        try:
            gender_str = data.get("gender").lower()
            birth_date_str = data.get("birth_date")
            birth_date = datetime.strptime(birth_date_str, "%d-%m-%Y")
            social_status_str = data.get("social_status").lower()
            magical_affinity_str = data.get("magical_affinity").lower()

            if gender_str == "hombre":
                gender = Profile.MALE
            elif gender_str == "mujer":
                gender = Profile.FAMELE
            else:
                err = {
                    "ERROR": "ValueError",
                    "Message": f"Field gender value '{gender_str}'' is required",
                    "userMessage": f"El valor campo gender '{gender_str}' es requerido",
                }
                logging.error(err.get("Message"))
                return Response(err, status=status.HTTP_400_BAD_REQUEST)

            if social_status_str == "plebeyo":
                social_status = Profile.COMMONER
            elif social_status_str == "noble":
                social_status = Profile.NOBLE
            else:
                err = {
                    "ERROR": "ValueError",
                    "Message": f"Field social status value '{social_status_str}' ",
                    "userMessage": f"El valor social status '{social_status_str}' no es valido",
                }
                logging.error(err.get("Message"))
                return Response(err, status=status.HTTP_400_BAD_REQUEST)

            Profile.objects.create(
                first_name=data["first_name"],
                last_name=data["last_name"],
                region=data["region"],
                birth_date=birth_date.date(),
                status=Profile.WAITING,
                gender=gender,
                social_status=social_status,
                magical_affinity=AFFINITY[magical_affinity_str],
            )

            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            logging.error(e)
            return Response(
                "Error en la solicitud de registro", status.HTTP_400_BAD_REQUEST
            )

    def put(
        self,
        request,
        uuid,
    ):
        profile = get_object_or_404(Profile, id=uuid)
        data = request.data
        birth_date_str = data.get("birth_date")
        if birth_date_str is not None:
            data["birth_date"] = datetime.strptime(birth_date_str, "%d-%m-%Y").date()

        serializer = ProfileSerializer(profile, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid):
        profile = get_object_or_404(Profile, id=uuid)
        profile.delete()
        return Response(status=status.HTTP_200_OK)

    def get(self, request, uuid):
        profile = get_object_or_404(Profile, id=uuid)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


class GetAllRegistration(ListAPIView):
    """
    Devuelve todos los registros
    """

    pagination_class = PageNumberPagination
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class GetAllGrimorios(ListAPIView):
    """
    Devuelve todos los registros
    """

    pagination_class = PageNumberPagination
    queryset = Grimorio.objects.all()
    serializer_class = GrimorioSerializer


class UpdateStatus(APIView):
    def put(self, request, uuid):
        profile = get_object_or_404(Profile, id=uuid)
        accepted = request.data.get("accepted")
        if type(accepted) is not bool:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if accepted:
            profile.status = Profile.ACCEPTED
        else:
            profile.status = Profile.DENIED
        profile.save()
        return Response(status=status.HTTP_200_OK)
