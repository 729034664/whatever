import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'zhang'
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # FLASKY_MAIL_SUBJECT_PREFIX = 'Flasky'
    # FLASKY_MAIL_SENDER = '729034664@qq.com'
    # FLASKY_ADMIN = os.environ.get('729034664@qq.com')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    #
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