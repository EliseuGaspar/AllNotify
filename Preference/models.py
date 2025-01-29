from django.db import models
from Users.models import User

from uuid import uuid4

class Preference(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='preferences')
    platform = models.CharField(max_length=50)
    notify = models.BooleanField(default=True)
    last_checked_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.platform} preferences for {self.user.email}"

