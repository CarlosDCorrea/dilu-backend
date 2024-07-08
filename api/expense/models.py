import uuid

from django.db import models
from django.conf import settings

from ..category.models import Category


class Expense(models.Model):
    expense_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    value = models.IntegerField()
    description = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
    category_name = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created = models.DateTimeField(auto_now_add=True)
    updatd = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.expense_id
