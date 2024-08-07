from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .service import (
    create as create_service,
    list_ as list_service
)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    return Response(**create_service(request))


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_(request):
    list_service(request)
    return Response()


@api_view(['UPDATE'])
@permission_classes([IsAuthenticated])
def update(request):
    return Response()


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request):
    return Response()
