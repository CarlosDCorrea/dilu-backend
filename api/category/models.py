import uuid

from django.db import models

from ..user.models import User


class Category(models.Model):
    category_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='The user that created this category', null=True)
    icon = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'categories'
        db_table = 'category'

    def __str__(self):
        return self.name
