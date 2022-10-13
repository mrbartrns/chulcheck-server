from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Attendance(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="user",
        related_name="attendence_datas",
    )
    timestamp = models.DateTimeField(verbose_name="timestamp", auto_now_add=True)

    def __str__(self):
        return f"{self.user} at {self.timestamp}"
