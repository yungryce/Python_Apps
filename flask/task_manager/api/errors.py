#!/usr/bin/python
from flask import request, jsonify


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