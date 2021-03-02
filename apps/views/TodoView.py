from flask import request, Response, Blueprint, json
from models.TodoModel import TodoModel, TodoSchema
from models import db

todo_api = Blueprint('todos', __name__)
todo_schema = TodoSchema()

@todo_api.route('/', methods=['GET'])
def get_all():
  todos = TodoModel.get_all()
  serialized = todo_schema.dump(todos, many=True)

  return custom_response(serialized, 200)

def custom_response(res, status_code):
  return Response(
    mimetype='application/json',
    response=json.dumps(res),
    status=status_code
  )