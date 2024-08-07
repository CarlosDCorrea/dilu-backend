from django.urls import path, re_path

from .views import (
    create,
    list_by_owner,
    update,
    delete,
    delete_several,
    get_by_owner,
    get_total_value,
    get_daily_graph
)


urlpatterns = [
    path('create', create, name='create-expense'),
    path('list-by-owner', list_by_owner, name='list-expense-by-owner'),
    path('update/<uuid:expense_id>', update, name='update-expense'),
    path('delete/<uuid:expense_id>', delete, name='delete-expense'),
    path('delete-several', delete_several, name='delete-several-expenses'),
    path('get-by-owner/<uuid:expense_id>', get_by_owner, name='get-expense-by-owner'),
    re_path(r'^total-value/(?P<start_date>\d{4}-\d{2}-\d{2})/(?P<end_date>\d{4}-\d{2}-\d{2})$',
            get_total_value,
            name='get-total-expenses'),
    re_path(r'^daily-graph/(?P<start_date>\d{4}-\d{2}-\d{2})/(?P<end_date>\d{4}-\d{2}-\d{2})$',
            get_daily_graph,
            name='get-daily-expenses-graph')
]
