from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def login(request):
    if request.method == 'POST':
        # LOGIN USER
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Welcome ' + username + '!!!')
            return redirect('dashboard')

        else:
            messages.error(request, 'Invalid Crendentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        # REGISTER USER
        # Getting forms values
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if password match
        if password == password2:
            # check username if exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email already exists')
                    return redirect('register')
                else:
                    # Everythings ok (saving user to db)
                    user = User.objects.create_user(
                        username=username, first_name=first_name, last_name=last_name, password=password, email=email)

                    # Login after register

                    # auth.login(request, user)
                    # messages.success(request, ' You are logged in !!!')
                    # return redirect('index')

                    # Redirect to login
                    user.save()
                    messages.success(
                        request, ' You are now registered and can log in !!!')
                    return redirect('login')

        else:
            messages.error(request, 'password does not match')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')