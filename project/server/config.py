import os
basedir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = 'sqlite:///'
database_name = 'diagnostic'


class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'diagnostic_secret')
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name + '_test.db'
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = 'c9e8a971a93b42e0f7132a7485b351a5cc63d122cee59b7580dfefb15bee5e47'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgres://vwwadmcfulsajn:c9e8a971a93b42e0f7132a7485b351a5cc63d122cee59b7580dfefb15bee5e47@ec2-52-207-90-231.compute-1.amazonaws.com:5432/d7arlu2c6lv7qe"
