from django.views import View
from django.shortcuts import render, redirect
from van.models.user import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail
from django.conf import settings



class ForgotPassword(View):
    def get(self, request):
        return render(request, 'forgot_password.html')

    def post(self, request):
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

            reset_link = 'click here'
            subject = 'Password reset request'
            message = f'Click the following link to reset your password: {reset_link}'
            from_email = settings.EMAIL_HOST_USER
            to_email = [email]
            #send_mail(subject, message, from_email, to_email, fail_silently=False)
        return redirect('forgot_password')
