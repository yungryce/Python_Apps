# Use the official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /api-flask-backend

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
COPY backend/ /api-flask-backend/
COPY config/ /api-flask-backend/config/
COPY models/ /api-flask-backend/models/
COPY requirements.txt /api-flask-backend/requirements.txt
COPY docker-compose.yml /api-flask-backend/docker-compose.yml

# Install dependencies
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Expose the port that Flask will run on
EXPOSE 5000

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
