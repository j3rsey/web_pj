class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://testuser:testpass@localhost:5432/testdb'.format()
        #url="arjuna.db.elephantsql.com", user='qlhiqtfa', pw='fyjXa1jFj30XpQ74CrxAn4Y-KsuROdGR', db='qlhiqtfa'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://testuser:testpass@localhost:5432/testdb'.format()
        #url="arjuna.db.elephantsql.com", user='qlhiqtfa', pw='fyjXa1jFj30XpQ74CrxAn4Y-KsuROdGR', db='qlhiqtfa'
