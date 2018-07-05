from django.contrib import messages
from django.contrib.auth import authenticate, login as dlogin, logout as dlogout
from django.shortcuts import render, redirect
from django.views import View

from users.forms import LoginForm, NewUserForm


class LoginView(View):

    def get(self, request):
        """
        Muestra el formulario de login
        :param request: Objeto httpRquest
        :return: Objeto HttpResponse con el render del formulario
         """

        form = LoginForm()

        context = {'form': form}
        messages.info(request, 'Introduzca usuario y contraseña para acceder a su cuenta')
        return render(request, 'users/login.html', context)

    def post(self, request):
        """
        Logea al usuario
        :param request: Objeto httpRquest
        :return: Objeto HttpResponse con el render del formulario
         """


        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Comprobamos credenciales
            user = authenticate(username=username, password=password)

            if user is None:
                messages.error(request, 'Usuario o contraseña incorrectos')
            else:
                # login de usuario
                dlogin(request, user)
                url = request.GET.get('next', 'home')
                return redirect(url)

        form = LoginForm()

        context = {'form': form}
        messages.info(request, 'Introduzca su usuario y contraseña para acceder a su cuenta')
        return render(request, 'users/login.html', context)

class LogoutView(View):

    def get(self, request):
        """
        Hace logout del usuario y redirige al login
        :param request: HttpRequest
        :return: HttpResponse y redirect a login
        """
        dlogout(request)
        return redirect('login')

class CreateUserView(View):

    def get(self, request):
        """
        Presenta el formulario de creación de un usuario
        :param request: objeto HttpRequest
        :return: HttpResponse con respuesta
        """

        form = NewUserForm()

        context = {'form': form}
        return render(request, 'users/new_user.html', context)

    def post(self, request):
        """
        Procesa el formulario de creación de un usuario
        :param request: objeto HttpRequest
        :return: HttpResponse con respuesta
        """

        form = NewUserForm(request.POST)
        if form.is_valid():
            new_user = form.save()

            form = NewUserForm()
            messages.success(request, 'Nuevo usuario creado correctamente')

        context = {'form': form}
        return render(request, 'users/new_user.html', context)
