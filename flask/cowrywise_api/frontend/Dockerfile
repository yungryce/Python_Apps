# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /api-flask-frontend

# Install pkg-config and other necessary build dependencies
RUN apt-get update && \
    apt-get install -y pkg-config \
                       build-essential \
                       python3-dev \
                       default-libmysqlclient-dev \
                       build-essential \
                       && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Copy the entire project directory
COPY frontend/ /api-flask-frontend/
COPY config/ /api-flask-frontend/config/
COPY models/ /api-flask-frontend/models/
COPY requirements.txt /api-flask-frontend/requirements.txt
COPY docker-compose.yml /api-flask-frontend/docker-compose.yml

# Install dependencies
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Expose port 5001 for frontend
EXPOSE 5001

# Command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
