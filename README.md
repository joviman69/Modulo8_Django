# Modulo8_Django

CORRECIONES A LA PRACTICA:
- INCLUIDA FECHA DE PUBLICACIÓN EN MODELO DE POST
- NO SON VISIBLES LOS POST QUE NO CORRESPONDAN AL USUARIO LOGUEADO O CON FECHA DE PUBLICACIÓN POSTERIOR A LA ACTUAL
- CREADO ARCHIVO requirements.txt
- ELIMINADO MENSAJE DE SUCCESS CONTRADICTORIO AL INTENTAR CREAR UN USUARIO CON USERNAME EXISTENTE
- ELIMINADAS LINEAS COMENTADAS OBSOLETAS DE ARCHIVO api.py (no era un error de GIT si no de COPY/PASTE) 
  
# Listado de endpoints incluidos en urls.py
# Project URls

  path('admin/', admin.site.urls),
  
  path('', HomeView.as_view(), name='home'),
  
  path('blogs/<str:username>/<int:pk>', PostDetailView.as_view(), name='post_detail'),
  
  path('blogs/', BlogListView.as_view()),
  
  path('blogs/<str:username>/', BlogDetailView.as_view()),
  
  path('login', LoginView.as_view(), name='login'),
  
  path('logout', LogoutView.as_view(), name='logout'),
  
  path('new-post', CreatePostView.as_view(), name='new_post'),
  
  path('new-blog', CreateBlogView.as_view(), name='new_blog'),
  
  path('signup', CreateUserView.as_view(), name='new_user'),
  

# API URLs

  path('api/v1/', include(router.urls)),
  
  path('api/v1/users/', UsersAPI.as_view(), name='api-user'),
  
  path('api/v1/users/<int:pk>/', UserDetailAPI.as_view(), name='api-user-detail'),
  
  path('api/v1/blogs/', BlogListAPI.as_view(), name='api-blogs'),
  


