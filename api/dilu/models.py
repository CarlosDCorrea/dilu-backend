import uuid

from django.db import models
from django.conf import settings
from django.utils import timezone


class Dilu(models.Model):
    dilu_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='dilus')
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        unique_together = ['owner', 'name']

    def __str__(self):
        return self.name
