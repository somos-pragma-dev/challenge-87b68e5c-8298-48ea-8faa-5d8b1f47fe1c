class HasRolePermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            user_roles = request.user.roles.all()
            required_role = getattr(view, 'required_role', None)
            if required_role and any(role.name == required_role for role in user_roles):
                return True
        return False


import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from.models import User