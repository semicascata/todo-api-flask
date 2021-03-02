import os
from app import create_app

'''
Before run:
  $ export FLASK_ENV=development
  $ export DATABASE_URL=postgresql+psycopg2://postgres:123123@127.0.0.1:5432/tododb
'''

env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)

if __name__ == '__main__':
  app.run()