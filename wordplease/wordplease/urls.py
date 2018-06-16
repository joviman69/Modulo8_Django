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

from blogs.views import blog_list
from posts.views import post_detail, last_posts, blog_detail, create_post
from users.views import login, logout, create_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', last_posts, name='home'),
    path('blogs/<str:username>/<int:pk>', post_detail, name='post_detail'),
    path('blogs', blog_list),
    path('blogs/<str:username>', blog_detail),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('new-post', create_post, name='new_post'),
    path('signup', create_user, name='new_user'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
