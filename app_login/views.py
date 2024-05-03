from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            print(user)
            messages.success(request, f'Login feito com sucesso!')
            print('logado')
            auth_login(request, user)
            return redirect('usuarios:usuarios')
        messages.error(request, 'Credencias invalidas')
        return redirect('login:login')
    return render(request, 'pages/login.html')