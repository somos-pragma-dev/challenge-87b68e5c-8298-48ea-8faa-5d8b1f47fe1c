class User(AbstractUser):
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'users'


from rest_framework import serializers
from.models import User