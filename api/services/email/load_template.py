from django.template.loader import render_to_string
from django.urls import reverse

from .core import send


def validate_user_template(request, username, email, user_id):
    subject = 'Welcome to the Django Authentication System'
    template_name = 'validate_user.html'
    activation_url = reverse('validate-user', args=(user_id,))
    absolute_activation_url = f"{request.scheme}://{request.get_host()}{activation_url}"
    context = {
        'username': username,
        'user_id': user_id,
        'activation_url': absolute_activation_url
    }

    template = render_to_string(template_name, context)
    title = 'Validar Creación de cuenta'
    return send(title, subject, template, email)
