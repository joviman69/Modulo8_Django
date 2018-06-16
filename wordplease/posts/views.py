from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from blogs.models import Blog
from posts.forms import PostForm
from posts.models import Post

class LastPost(View):

    def get(self, request):
        """
        Muestra el listado de los 5 últimos posts

        :param request: objeto HttpRequest
        :return: HttpResponse
        """

        # Recuperamos los 5 últimos post de la DB
        posts = Post.objects.filter(active=True).order_by('-creation_date')

        # Creamos contexto
        # messages.info(request, 'Últimos 5 posts')
        context = {'items': posts[:5]}

        # Devolver la respuesta utilizando una plantilla
        return render(request, 'posts/last_post.html', context)

class PostDetailView(View):

    def get(self, request, username, pk):
        """
        Muestra el detalle de un post
        :param request: objeto HttpRequest
        :param pk: post id
        :return: HttpResponse con respuesta
        """

        # Recuperamos el user.id de username

        try:
            userid = User.objects.get(username=username).id
            # un = User.objects.get(username=username).username

        except User.DoesNotExist:
            return HttpResponse('Requested username does not exist', status=404)

        # Obtenemos el blog del owner.id correspondiente al user.id

        try:
            blogid = Blog.objects.get(owner=userid).id

        except Blog.DoesNotExist:
            return HttpResponse('This username has any blog created', status=404)

        # Recuperamos el post de la DB correspondiente a pk

        try:
            post = Post.objects.filter(blog=blogid).get(pk=pk)

        except Post.DoesNotExist:
            return HttpResponse('Requested post does not exist for username ' + username + ' ' + '<a href="/">Regresar al inicio</a>' , status=404)

        # Creamos contexto
        context = {'post': post}

        # Devolver la respuesta utilizando una plantilla
        return render(request, 'posts/detail.html', context)

class BlogDetailView(View):
    def get(self, request, username):
        """
        Muestra los post de un blog
        :param request: objeto HttpRequest
        :param pk: post id
        :return: HttpResponse con respuesta
        """

        # Recuperamos el user.id y el owner.id
        try:
            userid = User.objects.get(username=username).id

        except User.DoesNotExist:
            return HttpResponse('Requested username does not exist', status=404)

        try:
            blogid = Blog.objects.get(owner=userid).id
            blogname = Blog.objects.get(owner=userid).name

        except Blog.DoesNotExist:
            return HttpResponse('Requested blog does not exist', status=404)


        # Recuperamos el id del blog correspondiente al username y sus posts de la DB
        try:
            post = Post.objects.select_related().filter(blog_id=blogid)

        except Post.DoesNotExist:
            return HttpResponse('Requested post does not exist', status=404)

        # Creamos contexto
        context = {'items': post, 'blog': blogname}

        # Devolver la respuesta utilizando una plantilla
        return render(request, 'posts/blog_posts.html', context)


# Si el usuario no está autenticado lo redirigimos al login

@method_decorator(login_required, name='dispatch')
class CreatePostView(View):

    def get(self, request):
        """
        Presenta el formulario de creación de un post
        :param request: objeto HttpRequest
        :return: HttpResponse con respuesta



        """
        form = PostForm()

        context = {'form': form}
        return render(request, 'posts/form.html', context)

    def post(self, request):
        """
        Procesa el formulario de creación de un post
        :param request: objeto HttpRequest
        :return: HttpResponse con respuesta



        """
        post = Post()
        userid = User.objects.get(username=request.user).id
        try:
            post.blog = Blog.objects.get(owner=userid)
        except Blog.DoesNotExist:
            return HttpResponse(
                'Este usuario no tiene creado ningún blog. <a href="/new-blog" %}>Cree un blog primero</a>',
                status=404)

        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            new_post = form.save()
            form = PostForm()
            messages.success(request, 'Post creado correctamente')


        context = {'form': form}
        return render(request, 'posts/form.html', context)
