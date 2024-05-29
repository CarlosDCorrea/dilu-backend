from django.urls import path

from .views import (
    create, list_, update, delete
)


urlpatterns = [
    path('create', create, name='create-user'),
    path('list', list_, name='list-users'),
    path('update', update, name='update-user'),
    path('delete', delete, name='delete-user')
]
