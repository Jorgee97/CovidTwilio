import os


class Config():
    DEBUG = False
    TESTING = False
    
    MONGODB_SETTINGS = {
        'db': os.environ.get('MONGO_DB') or 'covid_19',
        'host': os.environ.get('MONGO_HOST') or 'mongodb://localhost',        
    }


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False