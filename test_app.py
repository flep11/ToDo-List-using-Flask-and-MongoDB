import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_page_status_code(client):
    """Test dostępności strony głównej."""
    response = client.get('/')
    assert response.status_code == 200

def test_list_page_status_code(client):
    """Test dostępności strony z listą zadań."""
    response = client.get('/list')
    assert response.status_code == 200

def test_uncompleted_tasks_page_status_code(client):
    """Test dostępności strony z nieukończonymi zadaniami."""
    response = client.get('/uncompleted')
    assert response.status_code == 200

def test_completed_tasks_page_status_code(client):
    """Test dostępności strony z ukończonymi zadaniami."""
    response = client.get('/completed')
    assert response.status_code == 200

def test_about_page_status_code(client):
    """Test dostępności strony 'O aplikacji'."""
    response = client.get('/about')
    assert response.status_code == 200
