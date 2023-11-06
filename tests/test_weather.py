from fastapi.testclient import TestClient
from api.main import app


def create_user_and_make_login(username: str):
    """Create user and login to the DB.

    Args:
        username (str): Username

    Returns:
        str: Access token.
    """
    client = TestClient(app)

    user = {
        'email': f'{username}@testing.com',
        'username': username,
        'password': 'admin123'
    }

    response = client.post(
        '/api/v1/user/',
        json=user,
    )

    login = {
        'username': username,
        'password': 'admin123'
    }

    response = client.post(
        '/api/v1/login/',
        data=login,
        headers={
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        allow_redirects=True
    )

    data = response.json()
    return data['access_token']


def test_create_weather_element():
    """Create element in the DB"""
    token = create_user_and_make_login('test_create_weather_element')

    client = TestClient(app)

    element = {
                "comments": "My comments",
                "id": 1,
                "city_name": "test_city",
                "start_datetime": "2023-11-04T14:52:54.869802",
                "end_datetime": "2023-11-04T14:52:54.869835",
                "avg_temperature": 18,
                "latitude": 0,
                "longitude": 0
            }

    response = client.post(
        '/api/v1/weather/',
        json=element,
        headers={
            'Authorization': f'Bearer {token}'
        }
    )

    assert response.status_code == 201, response.text
    response = client.get(
            '/api/v1/weather/1',
            headers={
            'Authorization': f'Bearer {token}'
        }
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert data['city_name'] == element['city_name']


def test_delete_weather_element():
    """Delete element from the DB."""
    token = create_user_and_make_login('test_update_weather_ok')

    client = TestClient(app)
    ID = 2

    element = {
                "comments": "My comments",
                "id": ID,
                "city_name": "test_city",
                "start_datetime": "2023-11-04T14:52:54.869802",
                "end_datetime": "2023-11-04T14:52:54.869835",
                "avg_temperature": 18,
                "latitude": 0,
                "longitude": 0
            }

    response = client.post(
        '/api/v1/weather/',
        json=element,
        headers={
            'Authorization': f'Bearer {token}'
        }
    )

    assert response.status_code == 201, response.text

    response = client.delete(
        f'/api/v1/weather/{ID}',
        headers={
            'Authorization': f'Bearer {token}'
        }
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert data['msg'] == f'Element {ID} has been deleted successfully'
