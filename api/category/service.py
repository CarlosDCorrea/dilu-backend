from rest_framework import status

from .serializers import CategorySerializer
from .models import Category


def create(request):
    serializer = CategorySerializer(data=request.data)

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


def list_(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)

    response = {}

    response['data'] = serializer.data
    response['status'] = status.HTTP_200_OK
    return response


def update(request, category_id):
    pass


def delete(request, category_id):
    pass


def list_by_user(request):
    categories = Category.objects.filter(user=request.user)
    serializer = CategorySerializer(categories, many=True)

    response = {}
    response['data'] = serializer.data
    response['status'] = status.HTTP_200_OK
    return response


def get(request, category_id):
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
