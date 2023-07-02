from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(username, password)

        if user is not None:
            request.session['username'] = username
            login(request, user)
            return redirect('home')
        else:
            msg_error = 'Kredensial salah'
            print(msg_error)
            return render(request, 'login.html', {'error_message': msg_error})

    return render(request, 'login.html')
    

def home(request):
    if 'username' in request.session:
        username = request.session['username']
        return render(request, 'home.html', {'username': username})
    else:
        return redirect('login')


def logout_account(request):
    logout(request)
    return redirect("login")