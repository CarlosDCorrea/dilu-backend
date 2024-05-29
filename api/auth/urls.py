from django.urls import path

from .views import login, sign_up


urlpatterns = [
    path('login', login, name='login'),
    path('sign-up', sign_up, name='sign-up')
]
