

from rest_framework.permissions import BasePermission


class PostPermissions(BasePermission):

    def has_permission(self, request, view):
        """
        Define si el usuario puede realizar la acción (GET, POST, PUT, DELETE) sobre la vista view
        """
        return request.user.is_authenticated or request.method == 'GET'

    def has_object_permission(self, request, view, obj):
        """
        Define si el usuario puede realizar la acción sobre el objeto obj
        Un usuario puede borrar o actualizar un post, si es superuser o si el el propietario del post
        """
        return request.method == 'GET' or request.user.is_superuser or request.user == obj.owner
