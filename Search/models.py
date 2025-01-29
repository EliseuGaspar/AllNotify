from django.db import models
from Connections.models import Connection
from Users.models import User

from uuid import uuid4


class SearchIndex(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='search_indices')
    connection = models.ForeignKey(Connection, on_delete=models.CASCADE, related_name='search_indices')
    content = models.TextField()
    indexed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SearchIndex for {self.user.email} on {self.connection.platform}"
