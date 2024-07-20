from django.urls import path

from .views import (
    create,
    list_by_owner,
    update,
    delete,
    delete_several
)


urlpatterns = [
    path('create', create, name='create-expense'),
    path('list-by-owner', list_by_owner, name='list-by-owner-expense'),
    path('update/<uuid:expense_id>', update, name='update-expense'),
    path('delete/<uuid:expense_id>', delete, name='delete-expense'),
    path('delete-several', delete_several, name='delete-several-expenses'),
]
