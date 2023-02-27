from django.shortcuts import render, redirect
from van.models.user import User
from django.contrib.auth.hashers import make_password
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')
    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        password_again = postData.get('password_again')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        user = User(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)

        error_message = None
        if (not user.first_name):
            error_message = "First name Required !!"
        elif len(user.first_name) < 1:
            error_message = "First name must be more than one character"
        if (not user.last_name):
            error_message = "Last name Required !!"
        elif len(user.last_name) < 1:
            error_message = "Last name must be more than one character"
        elif not user.phone:
            error_message = "Phone number is required"
        elif len(user.phone) < 10:
            error_message = "Phone number Invalid"
        elif not user.password:
            error_message = "Password is required"
        elif len(user.password) < 6:
            error_message = "Password should be more than 6 characters"
        elif not password_again:
            error_message = "Please confirm password"
        elif not user.password == password_again:
            error_message = "Password does not match"

        isexists = user.isexists()
        if isexists:
            error_message = "Email already exists"

        if not error_message:
            user.password = make_password(user.password)
            user.register()
            return redirect('login')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)
