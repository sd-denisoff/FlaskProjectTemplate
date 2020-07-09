import os

# app config

CSRF_ENABLED = True
WTF_CSRF_ENABLED = True
SECRET_KEY = ''  # fill it

# email server config

MAIL_SERVER = ''  # fill it
MAIL_PORT = ''  # fill it
MAIL_USE_SSL = True
MAIL_USERNAME = ''  # fill it
MAIL_PASSWORD = ''  # fill it
MAIL_DEFAULT_SENDER = MAIL_USERNAME

# app server config

SERVER_IP = ''  # fill it
SERVER_LOGIN = ''  # fill it
SERVER_PASSWORD = ''  # fill it

# database config

MYSQL_USERNAME = ''  # fill it
MYSQL_PASSWORD = ''  # fill it
MYSQL_PORT = ''  # fill it
MYSQL_DB_NAME = ''  # fill it

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(basedir, 'database.db')  # for development only

# upload files config

ALLOWED_EXTENSIONS = {}  # fill it
