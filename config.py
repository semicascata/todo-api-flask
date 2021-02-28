import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
  DEBUG = False
  TESTING = False
  CSRF_ENABLED = True
  SECRET_KEY = 'th1s1sju5t4t35t'
