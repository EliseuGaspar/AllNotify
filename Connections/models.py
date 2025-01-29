from django.db import models
from Users.models import User

from uuid import uuid4


class Connection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='connections')
    platform = models.CharField(max_length=50)
    access_token = models.TextField()
    refresh_token = models.TextField(null=True, blank=True)
    connected_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.platform} - {self.user.email}"
