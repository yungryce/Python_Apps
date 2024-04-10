import os, jwt
from functools import wraps
from flask import request, jsonify
from models.users import UserModel
from models.blacklist import BlacklistToken


# Get the secret key from the environment variables
SECRET_KEY = os.getenv('SECRET_KEY')


def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
            if BlacklistToken.check_blacklist(token):
                return jsonify({'error': 'Token is blacklisted'}), 401
            request.token = token
        else:
            return jsonify({'error': 'Token is missing or invalid'}), 401
        try:
            # Decode and verify token
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            user_id = payload.get('sub')
            
            # Fetch user from database using user_id
            user = UserModel.query.get(user_id)

            # Attach user object to request for later use
            request.current_user = user
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401

        # Call the original function with any provided arguments
        return func(*args, **kwargs)

    return wrapper