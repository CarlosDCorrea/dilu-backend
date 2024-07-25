from django.urls import path

from .views import (
    create,
    list_by_owner,
    update,
    delete,
    delete_several,
    get_by_owner
)


urlpatterns = [
    path('create', create, name='create-expense'),
    path('list-by-owner', list_by_owner, name='list-expense-by-owner'),
    path('update/<uuid:expense_id>', update, name='update-expense'),
    path('delete/<uuid:expense_id>', delete, name='delete-expense'),
    path('delete-several', delete_several, name='delete-several-expenses'),
    path('get-by-owner/<uuid:expense_id>', get_by_owner, name='get-expense-by-owner')
]
