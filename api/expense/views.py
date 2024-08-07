from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .service import (
    create as create_service,
    list_by_owner as list_by_owner_service,
    update as update_service,
    delete as delete_service,
    delete_several as delete_several_service,
    get_by_owner as get_by_owner_service,
    get_total_value as get_total_value_service,
    get_daily_graph as get_daily_graph_service
)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    return Response(**create_service(request))


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_by_owner(request):
    # list_by_owner_service in this case do not returns a mapping object but a paginated response
    return list_by_owner_service(request)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update(request, expense_id):
    return Response(**update_service(request, expense_id))


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, expense_id):
    return Response(**delete_service(expense_id))


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_several(request):
    expenses_id = request.data
    return Response(**delete_several_service(expenses_id))


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_by_owner(request, expense_id):
    return Response(**get_by_owner_service(request, expense_id))


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_total_value(request, start_date, end_date):
    print('here 2')
    return Response(**get_total_value_service(request, start_date, end_date))


# Graphs
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_daily_graph(request, start_date, end_date):
    print('here')
    return Response(**get_daily_graph_service(request, start_date, end_date))
