from django.urls import path


from .views import (
    create,
    list_,
    list_by_user
)


urlpatterns = [
    path('create', create, name='create-category'),
    path('list', list_, name='list-all-categories'),
    path('list-by-user', list_by_user, name='list-categories-by-user'),
]
