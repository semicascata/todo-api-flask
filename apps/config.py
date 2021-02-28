import os
from dotenv import load_dotenv

# base path
BASE_DIR = os.path.dirname(__file__)

# dotenv
load_dotenv(os.path.join(BASE_DIR, '.env-local'))

postgres_uri = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
  user=os.getenv('PG_USER'),
  pw=os.getenv('PG_PASSWORD'),
  url=os.getenv('PG_URL'),
  db=os.getenv('PG_DB')
  )

class Config(object):
  DEBUG = False
  TESTING = False
  SQLALCHEMY_DATABASE_URI = postgres_uri
  SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
  DEBUG = True

class ProductionConfig(Config):
  pass

app_config = {
  'development': DevelopmentConfig,
  'production': ProductionConfig,
}