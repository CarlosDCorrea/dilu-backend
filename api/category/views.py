from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .service import (create as create_service,
                      list_ as list_service,
                      delete as delete_service,
                      list_by_user as list_by_user_service,
                      get as get_service)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    return Response(**create_service(request))


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_(request):
    return Response(**list_service(request))


@api_view(['UPDATE'])
@permission_classes([IsAuthenticated])
def update(request):
    pass


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, category_id):
    return Response(**delete_service(request, category_id))


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_by_user(request):
    return Response(**list_by_user_service(request))


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get(request, category_id):
    return Response(**get_service(request, category_id))
