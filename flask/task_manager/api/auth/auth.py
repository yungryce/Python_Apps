from flask import Blueprint, request, jsonify
from models.users import UserModel
from models.blacklist import BlacklistToken
from api.errors import validate_json
from api.auth.auth_utils import authenticate


auth_views = Blueprint("auth_views", __name__, url_prefix="/api/auth")


@auth_views.route('/register', methods=['POST'])
def register():
    """
    Create a new user.

    Returns:
        JSON response with the created user, or error response if validation fails
    """
    error = validate_json('username', 'email', 'password', 'first_name', 'last_name')
    if error:
        return error
    # Parse input data after validation
    data = request.get_json()
    username=data['username'],
    email=data['email']
    
    # Check if the username or email already exists
    if UserModel.get_first(username=username) or UserModel.get_first(email=email):
        return jsonify({'error': 'Username or Email already exists'}), 409
    
    # Proceed to create a new user since neither the username nor email are taken
    new_user = UserModel(
        username=username,
        email=email,
        password=data['password'],
        first_name=data['first_name'],
        last_name=data['last_name']
    )
    
    # Save the new user to the database
    try:
        new_user.save()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        # Handle any errors that occur during the save operation
        return jsonify({'error': 'Failed to register user'}), 500


@auth_views.route('/login', methods=['POST'])
def login():
    error = validate_json('username', 'password')
    if error:
        return error
    
    # Parse input data after validation
    data = request.get_json()
    username=data['username']

    user = UserModel.get_first(username=username)

    if user and user.check_password(data['password']):
        # Generate tokens
        token = user.generate_token()

        # Check if any token generation errors occurred
        if isinstance(token, Exception):
            return jsonify({'error': 'Failed to generate tokens'}), 500
        # Generate token

        # Check if the token is blacklisted
        if BlacklistToken.check_blacklist(token):
            return jsonify({'error': 'Token: Not allowed'}), 401

        # Serialize the user object to a JSON-compatible dictionary
        user_data = user.to_json()
        
        if user_data:
            return jsonify({
                'message': 'Login successful',
                'token': token,
                'user': user_data
            }), 200
        else:
            return jsonify({'error': 'Failed to serialize user data'}), 500
    else:
        return jsonify({'error': 'Invalid username or password'}), 401


@auth_views.route('/logout', methods=['POST'])
@authenticate
def logout():
    """
    Log out the current user.
    """
    token = request.token

    # Add the token to the blacklist
    try:
        blacklisted_token = BlacklistToken(token=token)
        blacklisted_token.save()
        return jsonify({'message': 'Logout successful'}), 200
    except Exception as e:
        return jsonify({'error': 'Failed to logout'}), 500
