from django.contrib.auth import authenticate

from rest_framework.authtoken.models import Token
from rest_framework import status

from ..user.models import User
from ..user.services import create


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

    return response


def sign_up(request):
    response_create = create(request)

    if response_create['status'] == 200:
        # Send email validation
        pass

    return response_create
