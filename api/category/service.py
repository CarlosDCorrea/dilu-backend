from rest_framework import status

from .serializers import CategorySerializer
from .models import Category


def create(data):
    serializer = CategorySerializer(data=data)

    response = {}

    if serializer.is_valid():
        category = serializer.save()
        print(type(category))
        response['data'] = {
            "message": f"Categoria creada satisfactoriamente {category}"
        }
        response['status'] = status.HTTP_201_CREATED
    else:
        response['data'] = {'error': serializer.errors}
        response['status'] = status.HTTP_400_BAD_REQUEST
    return response


def list_():
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)

    response = {}

    response['data'] = serializer.data
    response['status'] = status.HTTP_200_OK
    return response


def update(category_id, data):
    response = {}

    try:
        category = Category.objects.get(pk=category_id)
        serializer = CategorySerializer(instance=category, data=data, partial=True)

        response['data'] = {'update': serializer.data,
                            'message': 'Category updated successfully'}
        response['status'] = status.HTTP_200_OK
    except Category.DoesNotExist:
        response['data'] = {'message', 'The category does not exists'}
        response['status'] = status.HTTP_400_BAD_REQUEST
    finally:
        return response


def delete(category_id):
    response = {}

    try:
        Category.objects.get(pk=category_id).delete()

        response['data'] = {'message': 'Category deleted Successfully'}
        response['status'] = status.HTTP_200_OK
    except Category.DoesNotExist:
        response['data'] = {
            'message': 'No Category with the specified id found'}
        response['status'] = status.HTTP_400_BAD_REQUEST
    finally:
        return response


def get(category_id):
    response = {}
    try:
        category = Category.objects.get(pk=category_id)
        serializer = CategorySerializer(category)
        response['data'] = serializer.data
        response['status'] = status.HTTP_200_OK
    except Category.DoesNotExist as e:
        response['data'] = str(e)
        response['status'] = status.HTTP_400_BAD_REQUEST
    finally:
        return response
