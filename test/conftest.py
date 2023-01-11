import pytest
from app import creat_app


@pytest.fixture()
def app():
    app = creat_app()

    yield app


@pytest.fixture()
def client(app):
    client = app.test_client()
    yield client
