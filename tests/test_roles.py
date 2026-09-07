@pytest.mark.django_db
def test_create_role():
    client = APIClient()
    url = reverse('role-list')
    data = {'name': 'admin'}
    response = client.post(url, data, format='json')
    assert response.status_code == 201
    assert Role.objects.count() == 1


#!/usr/bin/env python
from django.core.management import execute_from_command_line