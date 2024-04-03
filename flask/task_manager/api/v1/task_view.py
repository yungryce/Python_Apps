#!/usr/bin/python3
"""
Task API endpoints.

This module defines API endpoints for managing tasks.

Endpoints:
    - GET /api/v1/tasks: Get all tasks
    - GET /api/v1/tasks/<task_id>: Get a specific task by ID
    - POST /api/v1/tasks: Create a new task
    - PUT /api/v1/tasks/<task_id>: Update an existing task
    - DELETE /api/v1/tasks/<task_id>: Delete a task
"""

from flask import abort, jsonify, request
from models.tasks import TaskModel
from api.v1 import app_views


def error_response(status_code, message):
    """
    Create a JSON error response.

    Args:
        status_code (int): HTTP status code
        message (str): Error message

    Returns:
        JSON response with error message and status code
    """
    response = jsonify({'error': message})
    response.status_code = status_code
    return response


def validate_json(*required_fields):
    """
    Validate JSON input.

    Args:
        *required_fields (str): Required fields

    Returns:
        Error response if validation fails, None otherwise
    """
    if not request.is_json:
        return error_response(400, 'Not a JSON')

    data = request.get_json()
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return error_response(400, f'Missing fields: {", ".join(missing_fields)}')
    return None


@app_views.route('/', methods=['GET'], strict_slashes=False)
def get():
    """
    Get all tasks.

    Returns:
        JSON response with all tasks
    """
    tasks = TaskModel.get_all()
    tasks_json = [task.to_json() for task in tasks]
    return jsonify(tasks_json)


@app_views.route('/<task_id>', methods=['GET'], strict_slashes=False)
def get_task(task_id):
    """
    Get a task by ID.

    Args:
        task_id (str): Task ID

    Returns:
        JSON response with the task, or 404 if not found
    """
    task = TaskModel.get_first(id=task_id)
    if not task:
        abort(404, description="Task not found")
    return jsonify(task.to_json())


@app_views.route('/', methods=['POST'], strict_slashes=False)
def create_task():
    """
    Create a new task.

    Returns:
        JSON response with the created task, or error response if validation fails
    """
    error = validate_json('title', 'description', 'done')
    if error:
        return error

    # Parse input data after validation
    data = request.get_json()
    task = TaskModel(
        title=data['title'],
        description=data['description'],
        done=data['done']
    )
    task.save()
    return jsonify(task.to_json()), 201


@app_views.route('/<task_id>', methods=['PUT'], strict_slashes=False)
def update_task(task_id):
    """
    Update an existing task.

    Args:
        task_id (str): Task ID

    Returns:
        JSON response with the updated task, or error response if validation fails or task not found
    """
    error = validate_json('title', 'description', 'done')
    if error:
        return error

    # Retrieve the task by ID
    task = TaskModel.get_first(id=task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    # Parse input data after validation
    data = request.get_json()

    # Update the task with the new values
    task.title = data['title']
    task.description = data['description']
    task.done = data['done']
    task.save()

    return jsonify(task.to_json()), 200


@app_views.route('/<task_id>', methods=['DELETE'], strict_slashes=False)
def delete_task(task_id):
    """
    Delete a task.

    Args:
        task_id (str): Task ID

    Returns:
        JSON response with success message, or error response if task not found
    """
    task = TaskModel.get_first(id=task_id)
    if not task:
        abort(404, description="Task not found")
    task.delete()
    return jsonify({'message': 'Task deleted successfully'}), 200
