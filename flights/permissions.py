from rest_framework.permissions import BasePermission
from datetime import datetime




class IsOwner(BasePermission):
    message = "You must be the Owner."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.user == request.user):
            return True
        else:
            return False


class three_days(BasePermission):
    message = "You can't."

    def has_object_permission(self, request, view, obj):

        if (obj.date - datetime.now().date()).days > 3:
            return True
        else:
            return False

