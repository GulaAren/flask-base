import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'almost-secret'
    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///%s' % (os.path.join(BASE_DIR, "db.sqlite"),)


class Develop(BaseConfig):
    DEBUG = True


class Testing(BaseConfig):
    DEBUG = True
    TESTING = True


class Production(BaseConfig):
    DEBUG = False
    TESTING = False


CONFIG_MAP = {
    'dev': Develop,
    'test': Testing,
    'prod': Production,
}
