from django.urls import path

from .views import (
    create,
    list_,
    update,
    delete
)


urlpatterns = [
    path('create', create, name='create-expense'),
    path('list', list_, name='list-expense'),
    path('update/<uuid:expense_id>', update, name='update-expense'),
    path('delete/<uuid:expense_id>', delete, name='delete-expense'),
]
