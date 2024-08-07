from django.contrib import admin

from .models import Dilu


@admin.register(Dilu)
class DiluAdmin(admin.ModelAdmin):
    list_display = (
        'dilu_id',
        'name',
        'owner',
        'created',
        'updated'
    )
