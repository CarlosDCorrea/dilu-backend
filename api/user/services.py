from typing import Dict

from django.shortcuts import render, redirect

from rest_framework import status

from .serializers import UserSerializer
from .models import User


def create(request) -> Dict[str, str | int | dict]:
    serializer = UserSerializer(data=request.data)

    response = {}

    if serializer.is_valid():
        serializer.save()

        print(f'serializer data:: {serializer.validated_data}')
        print(f'serializer data:: {serializer.data}')
        response['data'] = {
            "user": serializer.validated_data,
            "message": "usuario creado satisfactoriamente, verificate con tu correo"}
        response['status'] = status.HTTP_201_CREATED
    else:
        response['data'] = {'message_error': serializer.errors}
        response['status'] = status.HTTP_400_BAD_REQUEST

    return response


def list_all(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    response = {}
    response.data = serializer.data
    response.status_code = status.HTTP_200_OK

    return response


def activate(request, id):
    try:
        user = User.objects.get(id=id)
        user.is_active = True
        user.save()
        # TODO try using the id ass well
        return redirect('activate-user-success')
    except User.DoesNotExist:
        return redirect('activate-user-failure')


def activate_user_success(request):
    return render(request, "user/validate_user_success.html")


def activate_user_failure(request):
    return render(request, "user/validate_user_failure.html")
