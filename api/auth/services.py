from django.contrib.auth import authenticate

from rest_framework.authtoken.models import Token
from rest_framework import status

from ..user.models import User
from ..user.services import create

from ..services.email.load_template import validate_user_template


def login(request):
    email, password = request.data.values()

    response = {}

    try:
        user = authenticate(email, password)

        if not user:
            raise User.DoesNotExist()

        token = Token.objects.get(user=user)
        response['data'] = {'message': str(token)}
        response['status'] = status.HTTP_200_OK
    except User.DoesNotExist as e:
        response['data'] = {'message': str(e)}
    finally:
        return response


def sign_up(request):
    response_create = create(request)
    user = response_create['data']['user']
    if response_create['status'] == status.HTTP_201_CREATED:
        validate_user_template(request, user['username'], user['email'], user['id'])

    return response_create
