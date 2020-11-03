import os 

class Config:
   
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:accounts@localhost/accounts'


class prodConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:accounts@localhost/accounts'
    DEBUG = True

config_options={
    'development':DevConfig,
    'production':prodConfig,
    
}