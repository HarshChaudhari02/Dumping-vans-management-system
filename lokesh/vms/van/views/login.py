from django.views import View
from django.shortcuts import render, redirect

from van.models.user import User
from django.contrib.auth.hashers import  check_password

class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        user = User.get_user_by_email(email)
        password = request.POST.get('password')
        error_message = None
        if user:
            flag = check_password(password, user.password)
            if flag:
                request.session['user_id'] = user.id
                request.session['user_email'] = user.email
                request.session['user_fname'] = user.first_name
                request.session['user_lname'] = user.last_name
                request.session['user_phone'] = user.phone
                return redirect('homepage')
            else:
                error_message = "Email or Password Invalid"
        else:
            error_message = "Email or Password Invalid"

        return render(request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')