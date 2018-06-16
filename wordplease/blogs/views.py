from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from blogs.forms import BlogForm
from blogs.models import Blog

class BlogListView(View):

    def get(self, request):
        """
        Muestra el listado de los últimos blogs

        :param request: objeto HttpRequest
        :return: HttpResponse
        """

        # Recuperamos todos los blogs de la DB
        blogs = Blog.objects.filter(active=True).order_by('-creation_date')

        # Creamos contexto
        messages.info(request,'Listado de blogs')
        context = {'items': blogs}

        # Devolver la respuesta utilizando una plantilla
        return render(request, 'blogs/list.html', context)


# Decorador de login_required
@method_decorator(login_required, name='dispatch')
class CreateBlogView(View):


    def get(self, request):
        """
        Presenta el formulario de creación de un blog
        :param request: objeto HttpRequest
        :return: HttpResponse con respuesta
        """

        form = BlogForm()

        context = {'form': form}
        return render(request, 'blogs/form.html', context)


    def post(self, request):
        """
         Procesa el formulario de creación de un blog
        :param request: objeto HttpRequest
        :return: HttpResponse con respuesta
        """


        blog = Blog()
        try:
            blog.owner = User.objects.get(username=request.user)
        except Blog.DoesNotExist:
            return HttpResponse('Este usuario no existe', status=404)

        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            new_blog = form.save()
            form = BlogForm()
            messages.success(request, 'Blog creado correctamente')

        context = {'form': form}
        return render(request, 'blogs/form.html', context)

