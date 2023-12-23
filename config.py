import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    ENV_DB_NAME = os.getenv('MARIADB_DATABASE', 'finance')
    ENV_DB_USER = os.getenv('MARIADB_USER', 'finance')
    ENV_DB_PASS = os.getenv('MARIADB_PASSWORD', 'finance')
    ENV_DB_HOST = os.getenv('MARIADB_PASSWORD', 'db')

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + ENV_DB_USER + ':' + ENV_DB_PASS + '@' + ENV_DB_HOST + ':3306/' + ENV_DB_NAME
    SQLALCHEMY_TRACK_MODIFICATIONS = False