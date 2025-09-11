from django.db import models

from account_module.models import User


# Create your models here.


class UserImageUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_1 = models.ImageField(upload_to='user_uploads/')
    image_2 = models.ImageField(upload_to='user_uploads/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.submitted_at.strftime('%Y-%m-%d %H:%M')}"

