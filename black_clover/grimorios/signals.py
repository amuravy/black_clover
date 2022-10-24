import logging
from random import randrange

from django.db.models.signals import post_save
from django.dispatch import receiver

from black_clover.grimorios.models import Grimorio, Profile


@receiver(post_save, sender=Profile)
def create_grimorio(sender, instance, **kwargs):
    logging.info("SAVEEE")
    if instance.status == Profile.ACCEPTED:
        grimorio = Grimorio.objects.create(profile=instance, cover=randrange(1, 5))
        if grimorio.cover == 4:
            logging.info("UN GRIMORIO DE 4 HOJAAAAS!!!")
