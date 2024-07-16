from django.shortcuts import render, redirect

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .services import (create as create_service)
from .models import User


@api_view(http_method_names=['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    return Response(**create_service(request))


def list_all():
    pass


def update():
    pass


def delete():
    pass


@api_view(['GET'])
def validate(request, id):
    try:
        user = User.objects.get(id=id)
        user.is_active = True
        user.save()
        return redirect('validate-user-success')
    except User.DoesNotExist:
        return redirect('validate-user-failure')


@api_view()
def validate_user_success(request):
    return render(request, 'validate_user_success.html')


@api_view()
def validate_user_failure(request):
    return render(request, 'validate_user_failure.html')
