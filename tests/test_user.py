from fastapi.testclient import TestClient
from api.main import app

def test_create_user_ok():
    """Test user creation."""
    client = TestClient(app)

    user = {
        'email': 'test_create_user_ok@testing.com',
        'username': 'test_create_user_ok',
        'password': 'admin123'
    }

    response = client.post(
        '/api/v1/user/',
        json=user,
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data['email'] == user['email']
    assert data['username'] == user['username']


def test_create_user_duplicate_email():
    """Test user duplicated email."""
    client = TestClient(app)

    user = {
        'email': 'test_create_user_duplicate_email@testing.com',
        'username': 'test_create_user_duplicate_email',
        'password': 'admin123'
    }

    response = client.post(
        '/api/v1/user/',
        json=user,
    )
    assert response.status_code == 201, response.text

    user['username'] = 'test_create_user_duplicate_email2'

    response = client.post(
        '/api/v1/user/',
        json=user,
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data['detail'] == 'Email already registered'


def test_create_user_duplicate_username():
    """Test user duplicated username."""
    client = TestClient(app)

    user = {
        'email': 'test_create_user_duplicate_username@testing.com',
        'username': 'test_create_user_duplicate_username',
        'password': 'admin123'
    }

    response = client.post(
        '/api/v1/user/',
        json=user,
    )
    assert response.status_code == 201, response.text

    response = client.post(
        '/api/v1/user/',
        json=user,
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data['detail'] == 'Username already registered'


def test_login():
    """Test login."""
    client = TestClient(app)

    user = {
        'email': 'test_login@testing.com',
        'username': 'test_login',
        'password': 'admin123'
    }

    response = client.post(
        '/api/v1/user/',
        json=user,
    )
    assert response.status_code == 201, response.text

    login = {
        'username': 'test_login',
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

    assert response.status_code == 200, response.text
    data = response.json()
    assert len(data['access_token']) > 0
    assert data['token_type'] == 'bearer'
