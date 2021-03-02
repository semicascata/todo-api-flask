import os

class Config(object):
  DEBUG = False
  TESTING = False
  SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
  SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
  DEBUG = True

class ProductionConfig(Config):
  pass

app_config = {
  'development': DevelopmentConfig,
  'production': ProductionConfig,
}