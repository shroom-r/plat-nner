import os

class Config(object):
    TESTING = False

class ProductionConfig(Config):
    try:
        with open(os.environ.get("DATABASE_PASSWORD_FILE"), "r") as f:
            databasePassword = f.read()
            SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://root:{databasePassword}@db/plat_nner_db"
    except:
        pass

class DevelopmentConfig(Config):
    try:
        with open(os.environ.get("DATABASE_PASSWORD_FILE"), "r") as f:
            databasePassword = f.read()
            SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://root:{databasePassword}@db/plat_nner_db"
    except:
        pass

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    TESTING = True