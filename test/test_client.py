import os
import tempfile

import sys
sys.path.append('..')

from app import app

import pytest
pytest.main()

@pytest.fixture
def client():
    return app.test_client()

def test_query_get_all(client):
    response = client.get('/clients/v1/?q')
    assert len(response.json) > 0

def test_query_get_register_char(client):
    response = client.get('/clients/v1/?q=brian')
    assert len(response.data) > 0
    assert 'brian' in response.json[0]

def test_query_get_invalid_name(client):
    response = client.get('/clients/v1/?q=123')
    assert response.json == None
