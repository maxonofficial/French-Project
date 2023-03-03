from django.shortcuts import render

from django.urls import reverse_lazy
from django_rest_passwordreset.views import PasswordResetView

class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'email/password_reset_email.txt'
    success_url = reverse_lazy('password_reset_done')


