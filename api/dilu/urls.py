from django.urls import path

from .views import (
    create,
    list_,
    update,
    delete
)


urlpatterns = [
    path('create', create, name='create-dilu'),
    path('list', list_, name='list-dilu'),
    path('update', update, name='update-dilu'),
    path('delete', delete, name='delete-dilu'),
]
