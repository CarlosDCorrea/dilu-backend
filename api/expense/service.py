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
        serializer.save(user=request.user)

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


def list_by_owner(request):
    expenses = Expense.objects.filter(user=request.user)
    paginator = PageNumberPagination()

    paginated_queryset = paginator.paginate_queryset(expenses, request)
    serializer = ExpenseSerializer(paginated_queryset, many=True)

    return paginator.get_paginated_response(serializer.data)


def update(request, expense_id):
    response = {}

    try:
        expense = Expense.objects.get(pk=expense_id)
        serializer = ExpenseSerializer(
            instance=expense, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response['data'] = {'update': serializer.data,
                            'message': 'Expense updated successfully'}
        response['status'] = status.HTTP_200_OK
    except Expense.DoesNotExist as e:
        response['data'] = {
            'error': f"It was not possible to update the expense error: {e}"}
        response['status'] = status.HTTP_400_BAD_REQUEST
    except serializers.ValidationError as e:
        response['data'] = {'error': str(e)}
        response['status'] = status.HTTP_400_BAD_REQUEST
    except Exception as e:
        response['data'] = {'server error': str(e)}
        response['status'] = status.HTTP_400_BAD_REQUEST
    finally:
        return response


def delete(expense_id):
    response = {}

    try:
        Expense.objects.get(pk=expense_id).delete()

        response['data'] = {'message': 'Expense deleted successfully'}
        response['status'] = status.HTTP_200_OK
    except Expense.DoesNotExist:
        response['data'] = {'error': 'This expense does not exist'}
        response['status'] = status.HTTP_400_BAD_REQUEST
    finally:
        return response
