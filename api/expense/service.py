from rest_framework import serializers
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from .models import Expense
from .serializers import ExpenseSerializer


def create(request):
    serializer = ExpenseSerializer(data=request.data)

    response = {}

    try:
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response['data'] = {
            "message": "Expense created successfully"
        }
        response['status'] = status.HTTP_201_CREATED
    except serializers.ValidationError as e:
        response['data'] = {
            "error": f"It was not possible to create the expense errror: {e}"
        }
        response['status'] = status.HTTP_400_BAD_REQUEST
    except Exception as e:
        response['data'] = {
            "error": f'A not handled error ocurred {e} of type {type(e)}'
        }
        response['status'] = status.HTTP_500_INTERNAL_SERVER_ERROR
    finally:
        return response


def list_(request):
    expenses = Expense.objects.all()
    paginator = PageNumberPagination()

    paginated_queryset = paginator.paginate_queryset(expenses, request)
    serializer = ExpenseSerializer(paginated_queryset, many=True)

    return paginator.get_paginated_response(serializer.data)


def update(request, expense_id):
    response = {}
    print(request.data)
    try:
        expense = Expense.objects.get(pk=expense_id)
        serializer = ExpenseSerializer(
            instance=expense, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        print('serializer is valid')

        response['data'] = {'update': serializer.data,
                            'message': 'Expense updated successfully'}
        response['status'] = status.HTTP_200_OK
    except Expense.DoesNotExist as e:
        response['data'] = {
            'error': f"It was not possible to update the expense error: {e}"}
        response['status'] = status.HTTP_400_BAD_REQUEST
    except Exception as e:
        print("not handled error ocurred", str(e))
    finally:
        return response


def delete(expense_id):
    pass
