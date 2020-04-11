import os


class Config():
    DEBUG = False
    TESTING = False
    
    MONGODB_SETTINGS = {
        'db': os.environ.get('MONGO_DB') or 'covid_19',
        'host': os.environ.get('MONGO_HOST') or 'mongodb://localhost',        
    }

    DATOS_GOV_KEY = os.environ.get('DATOS_GOV_KEY')
    TWILIO_ML_API = os.environ.get('TWILIO_ML_API') or 'abcdefggjgdd'

class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False