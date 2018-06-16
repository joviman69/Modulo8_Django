from django.contrib import messages
from django.contrib.auth import authenticate, login as dlogin, logout as dlogout
from django.shortcuts import render, redirect

from users.forms import LoginForm, NewUserForm


def login(request):
    """
    Muestra el formulario de login y logea al usuario
    :param request: Objeto httpRquest
    :return: Objeto HttpResponse con el render del formulario
     """

    # Solo para peticiones POST
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Comprobamos credenciales
            user = authenticate(username=username, password=password)

            if user is None:
                messages.error(request, 'Wrong user or password')
            else:
                # login de usuario
                dlogin(request, user)
                return redirect('home')
    else:
        form = LoginForm()

    context = {'form': form}
    messages.info(request, 'Enter username and password for logging in your account')
    return render(request, 'users/login.html', context)

def logout(request):
    """
    Hace logout del usuario y redirige al login
    :param request: HttpRequest
    :return: HttpResponse y redirect a login
    """
    dlogout(request)
    return redirect('login')


def create_user(request):
    """
    Presenta el formulario de creación de un usuario y lo procesa
    :param request: objeto HttpRequest
    :return: HttpResponse con respuesta
    """
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            form = NewUserForm()
    else:
        form = NewUserForm()

    context = {'form': form}
    return render(request, 'users/new_user.html', context)
