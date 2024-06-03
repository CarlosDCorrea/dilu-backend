from django.urls import path

from .views import (
    create,
    list_all,
    update,
    delete,
    validate,
    validate_user_success,
    validate_user_failure
)


urlpatterns = [
    path('create', create, name='create-user'),
    path('list', list_all, name='list-all-users'),
    path('update', update, name='update-user'),
    path('delete', delete, name='delete-user'),
    path('validate/<int:id>', validate, name='validate-user'),
    path('validate-success', validate_user_success, name='validate-user-success'),
    path('validate-failure', validate_user_failure, name='validate-user-failure')
]
