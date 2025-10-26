"""
Unit tests for Flask Application
Tests all endpoints and edge cases
"""

import pytest
import json
from app import app


@pytest.fixture
def client():
    """Create test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_endpoint(client):
    """Test home endpoint returns API information"""
    response = client.get('/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'message' in data
    assert 'endpoints' in data
    assert data['version'] == '1.0.0'


def test_health_check(client):
    """Test health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'
    assert 'timestamp' in data


def test_get_all_tasks(client):
    """Test getting all tasks"""
    response = client.get('/api/tasks')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'tasks' in data
    assert 'count' in data
    assert isinstance(data['tasks'], list)


def test_get_specific_task(client):
    """Test getting a specific task by ID"""
    response = client.get('/api/tasks/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['id'] == 1
    assert 'title' in data
    assert 'completed' in data


def test_get_nonexistent_task(client):
    """Test getting a task that doesn't exist"""
    response = client.get('/api/tasks/999')
    assert response.status_code == 404
    data = json.loads(response.data)
    assert 'error' in data


def test_create_task(client):
    """Test creating a new task"""
    new_task = {
        'title': 'Test Task',
        'completed': False
    }
    response = client.post('/api/tasks',
                          data=json.dumps(new_task),
                          content_type='application/json')
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['title'] == 'Test Task'
    assert 'id' in data
    assert 'created_at' in data


def test_create_task_without_title(client):
    """Test creating a task without title fails"""
    new_task = {
        'completed': False
    }
    response = client.post('/api/tasks',
                          data=json.dumps(new_task),
                          content_type='application/json')
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data


def test_create_task_with_empty_body(client):
    """Test creating a task with empty body fails"""
    response = client.post('/api/tasks',
                          data=json.dumps({}),
                          content_type='application/json')
    assert response.status_code == 400


def test_update_task(client):
    """Test updating an existing task"""
    update_data = {
        'title': 'Updated Task',
        'completed': True
    }
    response = client.put('/api/tasks/1',
                         data=json.dumps(update_data),
                         content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['title'] == 'Updated Task'
    assert data['completed'] is True


def test_update_nonexistent_task(client):
    """Test updating a task that doesn't exist"""
    update_data = {
        'title': 'Updated Task'
    }
    response = client.put('/api/tasks/999',
                         data=json.dumps(update_data),
                         content_type='application/json')
    assert response.status_code == 404


def test_delete_task(client):
    """Test deleting a task"""
    response = client.delete('/api/tasks/2')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'message' in data


def test_delete_nonexistent_task(client):
    """Test deleting a task that doesn't exist"""
    response = client.delete('/api/tasks/999')
    assert response.status_code == 404
    data = json.loads(response.data)
    assert 'error' in data


def test_task_completion_toggle(client):
    """Test toggling task completion status"""
    # Create a task
    new_task = {'title': 'Toggle Test', 'completed': False}
    create_response = client.post('/api/tasks',
                                 data=json.dumps(new_task),
                                 content_type='application/json')
    task_id = json.loads(create_response.data)['id']
    
    # Toggle to completed
    update_data = {'completed': True}
    response = client.put(f'/api/tasks/{task_id}',
                         data=json.dumps(update_data),
                         content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['completed'] is True