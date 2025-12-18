import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    JSON_SORT_KEYS = False

class Development(Config):
    DEBUG = True

class Production(Config):
    DEBUG = False
