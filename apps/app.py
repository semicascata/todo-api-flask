from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import app_config

db = SQLAlchemy()

def create_app(env_name):
  app = Flask(__name__)
  app.config.from_object(app_config[env_name])
  db.init_app(app)

  # register blueprints

  @app.route('/', methods=['GET'])
  def index():
    message = 'ToDo API using Flask - Boilerplate Test, R. Drt'
    return jsonify(message=message)

  return app