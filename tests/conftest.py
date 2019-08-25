from app import my_app
import pytest


@pytest.fixture
def app():
    return my_app


@pytest.fixture
def client(app):
    return app.test_client()
