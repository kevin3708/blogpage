import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kevin:Password2@localhost/myblog'
    SECRET_KEY = 'mykey'
    QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kevin:Password2@localhost/myblog'

    

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kevin:Password2@localhost/myblog'
    
    DEBUG = True
    pass


config_options = {
'development':DevConfig,
'production':ProdConfig,
}