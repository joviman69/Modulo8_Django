"""wordplease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from blogs.views import BlogListView, CreateBlogView
from posts.views import PostDetailView, BlogDetailView, CreatePostView, HomeView
from users.views import LoginView, LogoutView, CreateUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('blogs/<str:username>/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('blogs', BlogListView.as_view()),
    path('blogs/<str:username>', BlogDetailView.as_view()),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('new-post', CreatePostView.as_view(), name='new_post'),
    path('new-blog', CreateBlogView.as_view(), name='new_blog'),
    path('signup', CreateUserView.as_view(), name='new_user'),



    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
