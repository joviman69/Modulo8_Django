from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.response import Response

from users.serializers import UserListSerializer, UserSerializer


class UsersAPI(GenericAPIView):

    queryset = User.objects.all()

    def get_serializer_class(self):
        return UserSerializer if self.request.method == 'POST' else UserListSerializer

    def get(self, request):
        """
        Devuelve el listado de usuarios en formato JSON
        :param request: objeto HttpRequest
        :return: Objeto HttpResponse en formato JSON
        """
        queryset = self.queryset
        users = self.paginate_queryset(queryset)
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(users, many=True)
        return self.get_paginated_response(serializer.data)



    def post(self, request):
        """
        Crea un usuario y devuelve su información
        :param request: objeto HttpRequest
        :return: objeto Response con los datos o 404 con errores
        """
        serializer_class = self.get_serializer_class()
        serializer =  serializer_class(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class UserDetailAPI(GenericAPIView):

    def get(self, request, pk):
        """
        Devuelve el detalle del usuario correspondiente al pk
        :param request: Objeto HttpRequest
        :param pk: pk del usuario
        :return: objeto Response con datos del usuario
        """
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


    def delete(self, request, pk):
        """
        Borra el usuario con el pk pasado
        :param request: objeto HttpRequest
        :param pk: pk del usuario a borrar
        :return: 204 o 404
        """
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        """
        Actualiza el usuario con el pk pasado
        :param request: objeto HttpRequest
        :param pk: pk del usuario a actualizar
        :return: 202 o 400
        """
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
