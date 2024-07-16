from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .service import (create as create_service,
                      list_ as list_service,
                      update as update_service,
                      delete as delete_service,
                      get as get_service)


# refer to https://www.django-rest-framework.org/api-guide/permissions/
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def create(request):
    return Response(**create_service(request))


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def list_(request):
    return Response(**list_service())


@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdminUser])
def update(request, category_id):
    data = request.data
    return Response(**update_service(category_id, data))


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete(request, category_id):
    return Response(**delete_service(category_id))


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get(request, category_id):
    return Response(**get_service(category_id))
