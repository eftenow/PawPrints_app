from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Comment(models.Model):
    comment_text = models.CharField(max_length=300)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_pet = models.ForeignKey('pets.Pet', on_delete=models.CASCADE)
    to_user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_time_of_publication']