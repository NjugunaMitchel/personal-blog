import os 

class Config:
    debug=True
    SECRETKEY = os.environ.get("SECRET_KEY")


class prodConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options={
    'development':DevConfig,
    'production':prodConfig
}