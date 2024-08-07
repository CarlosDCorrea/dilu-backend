from django.db.utils import IntegrityError
from django.db.models import Q

from rest_framework import status
from rest_framework.exceptions import ValidationError

from .serializers import DiluSerializer
from .models import Dilu


def create(request):
    response = {}

    serializer = DiluSerializer(data=request.data)

    try:
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)

        response['data'] = {'message': 'Dilu created successfully'}
        response['status'] = status.HTTP_201_CREATED
    except ValidationError as e:
        response['data'] = str(e)
        response['status'] = status.HTTP_400_BAD_REQUEST
    except IntegrityError as e:
        response['data'] = str(e)
        response['status'] = status.HTTP_400_BAD_REQUEST
    except Exception as e:
        response['data'] = f'un-handled error {e}'
        response['status'] = status.HTTP_500_INTERNAL_SERVER_ERROR
    finally:
        return response


# lists both owned and shared with ones
def list_(request):
    dilus = Dilu.objects.filter(
        Q(owner=request.user) | Q(participants=request.user))
    serializer = DiluSerializer(dilus, many=True)

    response = {}

    response['data'] = {
        'count': len(serializer.data),
        'results': serializer.data
    }
    response['status'] = status.HTTP_200_OK
    return response


def update(request, dilu_id):
    response = {}

    try:
        dilu = Dilu.objects.get(pk=dilu_id)
        serializer = DiluSerializer(dilu, data=request.data, partial=True)

        response['data'] = serializer.data
        response['status'] = status.HTTP_200_OK
    except Dilu.DoesNotExist:
        response['data'] = 'There is not a dilu with the specified id'
        response['status'] = status.HTTP_400_BAD_REQUEST
    finally:
        return response


def delete(dilu_id):
    response = {}

    try:
        Dilu.objects.get(pk=dilu_id).delete()

        response['data'] = {'message': 'Dilu updated successfully'}
        response['status'] = status.HTTP_200_OK
    except Dilu.DoesNotExist:
        response['data'] = 'There is not a dilu with the specified id'
        response['status'] = status.HTTP_400_BAD_REQUEST
    finally:
        return response
