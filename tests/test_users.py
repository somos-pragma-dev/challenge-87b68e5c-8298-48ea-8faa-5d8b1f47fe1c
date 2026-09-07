@pytest.mark.django_db
def test_create_user():
    client = APIClient()
    url = reverse('user-list')
    data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'testpassword'}
    response = client.post(url, data, format='json')
    assert response.status_code == 201
    assert User.objects.count() == 1


import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from.models import Role