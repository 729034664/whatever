import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SECRET_KEY = 'zhang'
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = '18519357162@163.com'
    MAIL_PASSWORD = 'zhangqiaosheng22'
    FLASKY_MAIL_SUBJECT_PREFIX = '标题'
    FLASKY_MAIL_SENDER = '18519357162@163.com'
    FLASKY_ADMIN = '18519357162@163.com'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_DEBUG = True

    FLASKY_POSTS_PER_PAGE = 10

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:////' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:////' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:////' + os.path.join(basedir, 'data.sqlite')

config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,

    'default':DevelopmentConfig
}