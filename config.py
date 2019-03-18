import os


CSRF_ENABLED = True
SECRET_KEY = 'nceufcne4yt3746t29oicwnoujwrucnw3454959uv'

basedir = os.path.abspath(os.path.dirname(__name__))
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.sqlite')
