from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .services import (create as create_service)


@api_view(http_method_names=['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    return Response(**create_service(request))


def list_():
    pass


def update():
    pass


def delete():
    pass
