from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .service import (
    create as create_service,
    list_ as list_service,
    update as update_service,
    delete as delete_service
)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    return Response(**create_service(request))


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_(request):
    return Response(**list_service(request))


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update(request, expense_id):
    return Response(**update_service(request, expense_id))


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, expense_id):
    return Response(**delete_service(expense_id))
