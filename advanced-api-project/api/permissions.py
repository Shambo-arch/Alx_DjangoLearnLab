from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Allow read-only access to everyone
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Write access is restricted to admins
        return request.user and request.user.is_staff

# Apply this permission to any view that requires admin-only write access

