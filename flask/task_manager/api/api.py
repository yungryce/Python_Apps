from flask import Blueprint
from flask_restful import Resource, Api, reqparse, abort

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


post_parsing = reqparse.RequestParser()
post_parsing.add_argument('title', type=str, required=True, help='Title cannot be blank!')
post_parsing.add_argument('description', type=str, required=True, help='Description cannot be blank!')
post_parsing.add_argument('done', type=bool, required=True, help='Done cannot be blank!')

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    
class ListTasks(Resource):
    def get(self):
        return tasks
    
class Task(Resource):
    def get(self, task_id):
        if task_id not in tasks:
            abort(400, message="Task does not exist")
        return tasks[task_id]
    
    def post(self, task_id):
        args = post_parsing.parse_args()
        
        # Check if task ID already exists
        if task_id in tasks:
            abort(400, message="Task ID already exists")

        # Add the new task to the tasks dictionary
        tasks[task_id] = {
            'title': args['title'],
            'description': args['description'],
            'done': args['done']
        }

        return tasks[task_id], 201
    
    def put(self, task_id):
        args = post_parsing.parse_args()

        # Check if task ID exists
        if task_id not in tasks:
            abort(400, message="Task does not exist")

        # Update the task with new values
        tasks[task_id]['title'] = args['title']
        tasks[task_id]['description'] = args['description']
        tasks[task_id]['done'] = args['done']

        # Return the updated task
        return tasks[task_id], 200  # 200 OK status code
    
    def delete(self, task_id):
        
        if task_id not in tasks:
            abort(400, message="Task does not exist")
            
        title_message = tasks[task_id]['title']

        del tasks[task_id]

        return {'task': title_message, 'message': f'Task deleted successfully'}, 201


api.add_resource(HelloWorld, '/api')
api.add_resource(ListTasks, '/api/tasks')
api.add_resource(Task, '/api/tasks/<int:task_id>')