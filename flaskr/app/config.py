import os
import secrets

class Config(object):
    TESTING = False
    try:
        # Read secretKey from .txt file. If no secret key is defined, define one
        # secret.txt file should be empty on first app run in order to generate automatically a secure secret
        with open("./app/secretKey.txt", "r+") as f:
            secret_key_temp = f.read()
            if not secret_key_temp:
                secret_key_temp = secrets.token_urlsafe(16)
                f.write(secret_key_temp)
            SECRET_KEY = secret_key_temp
    except Exception as e:
        print(repr(e))

class ProductionConfig(Config):
    try:
        with open(os.environ.get("DATABASE_PASSWORD_FILE"), "rw") as f:
            databasePassword = f.read()
            SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://root:{databasePassword}@db/plat_nner_db"
    except Exception as e:
        print(repr(e))

class DevelopmentConfig(Config):
    try:
        with open(os.environ.get("DATABASE_PASSWORD_FILE"), "r") as f:
            databasePassword = f.read()
            SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://root:{databasePassword}@db/plat_nner_db"
    except Exception as e:
        print(repr(e))

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    TESTING = True

