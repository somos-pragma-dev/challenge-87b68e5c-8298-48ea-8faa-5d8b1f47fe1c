class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'roles'


from rest_framework.permissions import BasePermission
from.models import Role