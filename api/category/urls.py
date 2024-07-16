from django.urls import path

from .views import (
    create,
    list_,
    delete,
    get
)


urlpatterns = [
    path('create', create, name='create-category'),
    path('list', list_, name='list-all-categories'),
    path('delete/<uuid:category_id>', delete, name='delete-category'),
    path('get/<uuid:category_id>', get, name='get-one-category')
]
