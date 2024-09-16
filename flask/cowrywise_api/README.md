cowryrise project assesment

# Setting up migration for backend and frontend services

### For Backend Service:
```
export FLASK_APP=backend.app
flask db init --directory migrations_backend
flask db migrate --directory migrations_backend
flask db upgrade --directory migrations_backend
```

### For Frontend Service:
```
export FLASK_APP=frontend.app
flask db init --directory migrations_frontend
flask db migrate --directory migrations_frontend
flask db upgrade --directory migrations_frontend
```


### Build Docker
```
sudo docker-compose build 
```

### Starting up docker
```
sudo docker-compose up -d
```