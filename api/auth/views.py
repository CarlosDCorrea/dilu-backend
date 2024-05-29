from rest_framework.response import Response
from rest_framework.decorators import api_view

from .services import (login as login_service,
                       sign_up as sign_up_service)


@api_view(http_method_names=['POST'])
def login(request):
    return Response(**login_service(request))


@api_view(http_method_names=['POST'])
def sign_up(request):
    return Response(**sign_up_service(request))
