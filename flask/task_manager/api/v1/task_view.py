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
from api.errors import validate_json
from api.auth.auth_utils import authenticate

# Modify the route to use the authentication decorator
@app_views.route('/', methods=['GET'], strict_slashes=False)
@authenticate
def get():
    # Retrieve the authenticated user from the request context
    user = request.current_user

    # Fetch all tasks related to the authenticated user
    tasks = user.tasks
    tasks_json = [task.to_json() for task in tasks]

    return jsonify(tasks_json), 200



@app_views.route('/<task_id>', methods=['GET'], strict_slashes=False)
@authenticate
def get_task(task_id):
    """
    Get a task by ID.

    Args:
        task_id (str): Task ID

    Returns:
        JSON response with the task, or 404 if not found
    """
    # Retrieve the authenticated user from the request context
    user = request.current_user

    # Fetch the task by ID
    task = TaskModel.get_first(id=task_id)
    # Check if the task exists and is associated with the authenticated user
    if not task or user not in task.users:
        return jsonify({'error': 'Task not found'}), 404

    return jsonify(task.to_json()), 200



@app_views.route('/', methods=['POST'], strict_slashes=False)
@authenticate
def create_task():
    """
    Create a new task.
    
    Args:
        task_id (str): Task ID

    Returns:
        JSON response with the created task, or error response if validation fails
    """
    error = validate_json('title', 'description', 'done')
    if error:
        return error

    # Parse input data after validation
    data = request.get_json()
    title = data['title']
    description = data['description']
    done = data['done']
    
    new_task = TaskModel(title=title, description=description, done=done)
    
    # Associate the task with the current user    
    user = request.current_user
    user.tasks.append(new_task)
    new_task.save()

    return jsonify(new_task.to_json()), 201


@app_views.route('/<task_id>', methods=['PUT'], strict_slashes=False)
@authenticate
def update_task(task_id):
    """
    Update an existing task.

    Args:
        task_id (str): Task ID

    Returns:
        JSON response with the updated task, or error response if validation fails or task not found
    """
    task = TaskModel.get_first(id=task_id)
    if not task:
        abort(404, description="Task not found")

    error = validate_json('title', 'description', 'done')
    if error:
        return error

    # Parse input data after validation
    data = request.get_json()
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
