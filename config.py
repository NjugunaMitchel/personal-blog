import os 

class Config:
   
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:accounts@localhost/accounts'


class prodConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:accounts@localhost/accounts'
    DEBUG = True

config_options={
    'development':DevConfig,
    'production':prodConfig,
    
}