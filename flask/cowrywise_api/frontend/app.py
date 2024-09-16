#!/usr/bin/python3
import os
from dotenv import load_dotenv
from flask import Flask, request
from flask_migrate import Migrate

from config.base_database import db, init_db
from config.config import setup_logging
from config.error_handlers import register_error_handlers
from api.v1.frontend import frontend_bp


# Load environment variables from .env file
load_dotenv()

# Start the Flask app
app = Flask(__name__)

# Load configuration based on the environment
env = os.getenv('FLASK_ENV', 'development')
if env == 'production':
    app.config.from_object('config.config.ProductionConfig')
else:
    app.config.from_object('config.config.DevelopmentConfig')

# Set up logging
setup_logging(app)

# Register error handlers
register_error_handlers(app)

# Initialize SQLAlchemy with the Flask app
init_db(app)
Migrate(app, db)

# Register the Blueprint with the Flask application
app.register_blueprint(frontend_bp)

# Log request information before each request
@app.before_request
def log_request_info():
    app.logger.info('Request: %s %s %s', request.method, request.url, request.data)

# Log response information after each request
@app.after_request
def log_response_info(response):
    app.logger.info('Response: %s %s', response.status, response.get_data(as_text=True))
    return response

if __name__ == '__main__':
    host = os.getenv('HOST', '0.0.0.0')
    port = os.getenv('PORT', '5001')
    app.run(host=host, port=port, debug=(env == 'development'))