from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Organization(models.Model):
    name = models.CharField(verbose_name="name", max_length=25)
    leader = models.ForeignKey(
        User, verbose_name="leader", on_delete=models.SET_NULL, null=True
    )
    members = models.ManyToManyField(User, related_name="organizations", blank=True)
    created_at = models.DateTimeField(verbose_name="created_at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="updated_at", auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Attendance(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="user",
        related_name="attendance_data",
    )
    organization = models.ForeignKey(
        Organization, on_delete=models.SET_NULL, null=True, related_name="attendances"
    )
    timestamp = models.DateTimeField(verbose_name="timestamp", auto_now_add=True)

    class Meta:
        ordering = ["timestamp"]

    def __str__(self):
        return f"{self.user} at {self.timestamp}"
