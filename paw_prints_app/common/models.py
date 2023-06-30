from django.contrib.auth import get_user_model
from django.db import models

from paw_prints_app.pets.models import Pet

UserModel = get_user_model()



class Notification(models.Model):
    recipient = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


class Comment(models.Model):
    comment_text = models.CharField(max_length=300)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    to_user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_time_of_publication']