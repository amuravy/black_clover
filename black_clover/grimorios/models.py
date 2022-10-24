import uuid

from django.db import models


# Create your models here.
class Profile(models.Model):
    """
    Represents the persistent information about a user, this id is used system-wide
    """

    WAITING = "En espera de aprobacion"
    DENIED = "denied"
    ACCEPTED = "accepted"

    COMMONER = 1
    NOBLE = 2

    MALE = 1
    FAMELE = 2

    DARKNESS = 1
    LIGHT = 2
    FIRE = 3
    WATER = 4
    WIND = 5
    EARTH = 6

    GENDER_DICT = {"Hombre": 1, "Mujer": 2}

    STATUS = [(WAITING, "En espera"), (DENIED, "Denegado"), (ACCEPTED, "Aceptado")]
    MAGICAL_AFFINITY = [
        (DARKNESS, "Oscuridad"),
        (LIGHT, "Luz"),
        (FIRE, "Fuego"),
        (WATER, "Agua"),
        (WIND, "Viento"),
        (EARTH, "Tierra"),
    ]
    GENDER_CHOICES = [
        (MALE, "Hombre"),
        (FAMELE, "Mujer"),
    ]
    SOCIAL_STATUS = [
        (COMMONER, "Plebeyo"),
        (NOBLE, "Noble"),
    ]

    # Personalmente me gusta màs uuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(
        max_length=20,
    )
    last_name = models.CharField(
        max_length=20,
    )
    region = models.CharField(max_length=40, null=True, blank=True)

    birth_date = models.DateField(null=True, blank=True)
    # Considero màs apropiado poner la fecha de nacimiento.
    status = models.CharField(max_length=100, choices=STATUS, default=WAITING)

    gender = models.PositiveIntegerField(choices=GENDER_CHOICES)
    social_status = models.PositiveIntegerField(choices=SOCIAL_STATUS)
    magical_affinity = models.PositiveIntegerField(choices=MAGICAL_AFFINITY)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.full_name}"


class Grimorio(models.Model):
    SINCERITY = 1
    HOPE = 2
    LOVE = 3
    GOOD_LUCK = 4
    HOPELESS = 5
    COVER = [
        (SINCERITY, "Sinceridad"),
        (HOPE, "Desesperanza"),
        (LOVE, "Amor"),
        (GOOD_LUCK, "Buena suerte"),
        (HOPELESS, "Desesperanza"),
    ]
    profile = models.ForeignKey(
        Profile,
        related_name="grimorio",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    cover = models.PositiveIntegerField(choices=COVER)

    def __str__(self):
        return f"{self.get_cover_display()}"
