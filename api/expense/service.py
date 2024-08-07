from django.db.models import Sum

from rest_framework import serializers
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from .models import Expense
from .serializers import ExpenseSerializer


def create(request):
    request.data['created'] = request.data['created'].split('T')[0]
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
        print('==================================')
        print(e.detail)
        print(type(e.detail))
        response['data'] = e.detail
        response['status'] = status.HTTP_400_BAD_REQUEST
    except Exception as e:
        response['data'] = e
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
    request.data['created'] = request.data['created'].split('T')[0]

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


def delete_several(expenses_id):
    response = {}

    count, _ = Expense.objects.filter(pk__in=expenses_id).delete()

    if not expenses_id:
        # delete() fails therefore it uses else's status code
        response['data'] = {'error': 'No expenses id list provided'}

    if count:
        response['data'] = {'count': count}
        response['status'] = status.HTTP_200_OK
    else:
        response['data'] = {'error': 'No expenses to delete found'}
        response['status'] = status.HTTP_400_BAD_REQUEST
    return response


def get_by_owner(request, expense_id):
    response = {}

    try:
        expense = Expense.objects.get(pk=expense_id, user=request.user)
        serializer = ExpenseSerializer(expense)

        response['data'] = serializer.data
        response['status'] = status.HTTP_200_OK
    except Expense.DoesNotExist:
        response['data'] = 'The expense does not exists'
        response['status'] = status.HTTP_400_BAD_REQUEST
    except Exception as e:
        response['data'] = f'Error not handled {e}'
        response['status'] = status.HTTP_500_INTERNAL_SERVER_ERROR
    finally:
        return response


def get_total_value(request, start_date, end_date):
    response = {}

    total_value = Expense.objects.filter(
        user=request.user, created__range=(start_date, end_date)).aggregate(total=Sum('value', default=0))

    response['data'] = total_value
    response['status'] = status.HTTP_200_OK
    return response


# GRAPHS
def get_daily_graph(request, start_date, end_date):
    response = {}

    expenses = Expense.objects.filter(
        user=request.user,
        created__range=(start_date, end_date)).values('created').annotate(value=Sum('value'))

    print(expenses)

    response['data'] = expenses
    response['status'] = status.HTTP_200_OK
    return response
