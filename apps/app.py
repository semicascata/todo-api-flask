from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import app_config
from models import db
from views.TodoView import todo_api as todo_blueprint 

# db = SQLAlchemy()

def create_app(env_name):
  app = Flask(__name__)
  app.config.from_object(app_config[env_name])
  db.init_app(app)

  # register blueprints
  app.register_blueprint(todo_blueprint, url_prefix='/api/v1/todos')

  @app.route('/', methods=['GET'])
  def index():
    message = 'ToDo API using Flask - Boilerplate Test, R. Drt'
    return jsonify(message=message)

  return app