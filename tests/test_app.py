import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
from app import app
import json

def test_get_todos():
    client = app.test_client()
    response = client.get('/todos')
    assert response.status_code == 200
    assert json.loads(response.data) == []

def test_add_todo():
    client = app.test_client()
    response = client.post('/todos', json={'task': 'Test task'})
    assert response.status_code == 201
    assert json.loads(response.data) == {'task': 'Test task'}
