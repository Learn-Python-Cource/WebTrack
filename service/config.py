import os

basedir = os.path.abspath(os.path.dirname(__file__))


WEATHER_DEFAULT_CITY = 'Moscow,Russia'
WEATHER_API_KEY = '4375ed2187ac4207a4a62831222703'
PAGE_TITLE = 'WEB TRACK LP24'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
print(SQLALCHEMY_DATABASE_URI)
