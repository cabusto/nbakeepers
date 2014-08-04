import os

#default config
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = "*/\xe3\xf4$\xa6\x16\x14\xac\xad#\xe6$\x85\xec\'\x8c\x8a\xf3t\xe8="
	STORMPATH_API_KEY_FILE = '~/.stormpath/apiKey.properties'
	STORMPATH_APPLICATION = 'nbakeepers'
	STORMPATH_ENABLE_GIVEN_NAME = False
	STORMPATH_ENABLE_MIDDLE_NAME = False
	STORMPATH_ENABLE_SURNAME = False
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False