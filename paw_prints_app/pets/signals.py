from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver

from paw_prints_app.pets.models import Pet

UserModel = get_user_model()


@receiver(pre_save, sender=Pet)
def set_added_by(sender, instance, **kwargs):
    if not instance.added_by:
        instance.added_by = UserModel.objects.get(username=instance.request.user.username)
