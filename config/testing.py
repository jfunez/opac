# coding: utf-8

"""
    Configuração para o ambiente de testing
"""

TESTING = True
DEBUG = False
ASSETS_DEBUG = DEBUG
OPAC_COLLECTION = 'DUMMY_TEST'
SECRET_KEY = 'a-dummy-testing-secret'


# SQL Alchemy
DATABASE_FILE = 'TESTING_opac_admin.sqlite'
DATABASE_DIR = '/tmp'  # Absoulte path
DATABASE_PATH = '%s/%s' % (DATABASE_DIR, DATABASE_FILE)
SQLALCHEMY_DATABASE_URI = 'sqlite:////%s' % DATABASE_PATH
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

MONGODB_SETTINGS = {
    'db': 'TESTING_OPAC_MONGO',
    'host': '127.0.0.1',
    'port': 27017
}

# envio de emails
MAIL_SERVER = 'localhost'
MAIL_PORT = 1025
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_DEBUG = DEBUG
MAIL_USERNAME = None
MAIL_PASSWORD = None
MAIL_DEFAULT_SENDER = 'webmaster.test@opac.scielo.org'
MAIL_MAX_EMAILS = None
# MAIL_SUPPRESS_SEND = default app.testing
MAIL_ASCII_ATTACHMENTS = False

DEBUG_TB_INTERCEPT_REDIRECTS = False