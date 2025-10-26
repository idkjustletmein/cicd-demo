"""
Flask Web Application for CI/CD Pipeline Demo
A simple REST API with basic CRUD operations
"""

from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# In-memory data store
tasks = [
    {"id": 1, "title": "Setup CI/CD Pipeline", "completed": False, "created_at": "2025-01-15"},
    {"id": 2, "title": "Write Unit Tests", "completed": False, "created_at": "2025-01-15"}
]

task_id_counter = 3


@app.route('/')
def home():
    """Home endpoint with API information"""
    return jsonify({
        "message": "Welcome to CI/CD Demo API",
        "version": "1.0.0",
        "endpoints": {
            "GET /": "API information",
            "GET /health": "Health check",
            "GET /api/tasks": "Get all tasks",
            "GET /api/tasks/<id>": "Get specific task",
            "POST /api/tasks": "Create new task",
            "PUT /api/tasks/<id>": "Update task",
            "DELETE /api/tasks/<id>": "Delete task"
        }
    })


@app.route('/health')
def health():
    """Health check endpoint for monitoring"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }), 200


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    return jsonify({
        "tasks": tasks,
        "count": len(tasks)
    }), 200


@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Get a specific task by ID"""
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    
    return jsonify(task), 200


@app.route('/api/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    global task_id_counter
    
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({"error": "Title is required"}), 400
    
    new_task = {
        "id": task_id_counter,
        "title": data['title'],
        "completed": data.get('completed', False),
        "created_at": datetime.now().strftime("%Y-%m-%d")
    }
    
    tasks.append(new_task)
    task_id_counter += 1
    
    return jsonify(new_task), 201


@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Update an existing task"""
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    
    data = request.get_json()
    
    if 'title' in data:
        task['title'] = data['title']
    if 'completed' in data:
        task['completed'] = data['completed']
    
    return jsonify(task), 200


@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task"""
    global tasks
    
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    
    tasks = [t for t in tasks if t['id'] != task_id]
    
    return jsonify({"message": "Task deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)